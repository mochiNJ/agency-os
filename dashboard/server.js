// Agency — Agency Dashboard
// Dependency-free Node server. Reads the live clients/ folder and serves a nice UI.
// Run:  node dashboard/server.js   →   http://localhost:4321
'use strict';

const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const ROOT = path.resolve(__dirname, '..');          // the "AI Agency" repo root
const CLIENTS_DIR = path.join(ROOT, 'clients');
const PORT = process.env.DASH_PORT || 4321;

const REGISTRY = {
  // Per-client DISPLAY metadata only (label, colour, icon). Add an entry per client as
  // you onboard them; a client with no entry still renders, with defaults.
  // The SOURCE OF TRUTH for who is a client and what state they are in is
  // system/active-clients.md. Keep this block to presentation.
};

const DOC_MAP = [
  { file: 'brand-profile.md',      label: 'Brand Profile',       icon: '◆', group: 'Foundation' },
  { file: 'visual-identity.md',    label: 'Visual Identity',     icon: '❖', group: 'Foundation' },
  { file: 'competitor-report.md',  label: 'Competitor Research', icon: '⬡', group: 'Research' },
  { file: 'trend-report.md',       label: 'Trend Research',      icon: '⬢', group: 'Research' },
  { file: 'seo-aeo-report.md',     label: 'SEO / AEO Audit',     icon: '⬠', group: 'Research' },
  { file: 'content-calendar.md',   label: 'Content Calendar',    icon: '▦', group: 'Content' },
  { file: 'video-remarks.md',      label: 'Video Rules',         icon: '▶', group: 'Content' },
];

const IMG_EXT = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'];
const VID_EXT = ['.mp4', '.mov', '.webm', '.m4v'];
const PDF_EXT = ['.pdf'];

function safeJoin(base, target) {
  const p = path.resolve(base, '.' + path.sep + target.replace(/^([/\\])+/, ''));
  if (!p.startsWith(base)) return null;
  return p;
}
function prettify(id) { return id.replace(/[-_]/g, ' ').replace(/\b\w/g, c => c.toUpperCase()); }

// Paths follow system/file-system-law.md. They changed on 2026-09-06 when uploads/,
// assets/ and content/ were abolished; this file was NOT updated with them and quietly
// showed every client as having no logo and no assets. sync.py never caught it because
// it only link-checks .md files. structure-check.py now scans code too.
function findLogo(id) {
  const logoDir = path.join(CLIENTS_DIR, id, 'brand', 'logo');
  try {
    const f = fs.readdirSync(logoDir).find(n => IMG_EXT.includes(path.extname(n).toLowerCase()));
    if (f) return `/raw/${encodeURIComponent(id)}/brand/logo/${encodeURIComponent(f)}`;
  } catch {}
  return null;
}

function listClients() {
  let dirs = [];
  try {
    dirs = fs.readdirSync(CLIENTS_DIR, { withFileTypes: true }).filter(d => d.isDirectory()).map(d => d.name);
  } catch {}
  return dirs.map(id => {
    const meta = Object.assign(
      { name: prettify(id), type: 'Client', status: 'active', goal: '', location: '', accent: '#e0723a' },
      REGISTRY[id] || {}
    );
    const override = path.join(CLIENTS_DIR, id, 'dashboard.json');
    if (fs.existsSync(override)) { try { Object.assign(meta, JSON.parse(fs.readFileSync(override, 'utf8'))); } catch {} }
    meta.id = id;
    meta.logo = findLogo(id);
    meta.docCount = DOC_MAP.filter(d => fs.existsSync(path.join(CLIENTS_DIR, id, d.file))).length;
    meta.postCount = parseCalendar(id).length;
    return meta;
  });
}

function walk(dir, cb, depth = 0) {
  if (depth > 4) return;
  let entries = [];
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return; }
  for (const e of entries) {
    if (e.name === 'node_modules' || e.name.startsWith('.')) continue;
    const abs = path.join(dir, e.name);
    if (e.isDirectory()) walk(abs, cb, depth + 1);
    else cb(abs);
  }
}

function clientDetail(id) {
  const base = path.join(CLIENTS_DIR, id);
  if (!fs.existsSync(base)) return null;
  const docs = DOC_MAP.filter(d => fs.existsSync(path.join(base, d.file)))
    .map(d => ({ ...d, path: `/raw/${encodeURIComponent(id)}/${d.file}` }));

  // A product is now a FOLDER holding product.md, not a loose .md file.
  let products = [];
  try {
    products = fs.readdirSync(path.join(base, 'products'), { withFileTypes: true })
      .filter(d => d.isDirectory() && !d.name.startsWith('_'))
      .filter(d => fs.existsSync(path.join(base, 'products', d.name, 'product.md')))
      .map(d => ({ label: prettify(d.name), icon: '▪',
        path: `/raw/${encodeURIComponent(id)}/products/${encodeURIComponent(d.name)}/product.md` }));
  } catch {}

  const assets = { images: [], videos: [], pdfs: [] };
  // brand/ = identity, products/ = everything about a product, library/posts/ = finished work.
  // pipeline/ is deliberately excluded: it holds work in motion, which must drain to empty.
  for (const sub of ['brand', 'products', 'library/posts']) {
    walk(path.join(base, sub), (abs) => {
      const rel = path.relative(base, abs).split(path.sep).map(encodeURIComponent).join('/');
      const ext = path.extname(abs).toLowerCase();
      const item = { name: path.basename(abs), path: `/raw/${encodeURIComponent(id)}/${rel}` };
      if (IMG_EXT.includes(ext)) assets.images.push(item);
      else if (VID_EXT.includes(ext)) assets.videos.push(item);
      else if (PDF_EXT.includes(ext)) assets.pdfs.push(item);
    });
  }
  const meta = listClients().find(c => c.id === id) || { id, name: prettify(id) };
  return { ...meta, docs, products, assets };
}

// ---------- Content-calendar parsing → drag-and-drop events ----------
function overridePath(id) {
  const dir = path.join(CLIENTS_DIR, id, '.dashboard');
  return { dir, file: path.join(dir, 'schedule-overrides.json') };
}
function readOverrides(id) {
  try { return JSON.parse(fs.readFileSync(overridePath(id).file, 'utf8')); } catch { return {}; }
}
function writeOverride(id, evId, date) {
  const { dir, file } = overridePath(id);
  try { fs.mkdirSync(dir, { recursive: true }); } catch {}
  const cur = readOverrides(id);
  cur[evId] = date;
  fs.writeFileSync(file, JSON.stringify(cur, null, 2));
}

function stripMd(s) {
  return (s || '').replace(/\*\*/g, '').replace(/`/g, '').replace(/\[(.*?)\]\(.*?\)/g, '$1').trim();
}
const PLATFORM_COLORS = {
  Instagram: '#e1447f', TikTok: '#26c6c9', Facebook: '#5a86ff', YouTube: '#ff4d4d', default: '#e0723a',
};
function platformOf(cell) {
  const c = (cell || '').toLowerCase();
  if (c.includes('instagram')) return 'Instagram';
  if (c.includes('tiktok')) return 'TikTok';
  if (c.includes('facebook')) return 'Facebook';
  if (c.includes('youtube')) return 'YouTube';
  return 'Other';
}

function parseCalendar(id) {
  const file = path.join(CLIENTS_DIR, id, 'content-calendar.md');
  let txt = '';
  try { txt = fs.readFileSync(file, 'utf8'); } catch { return []; }
  const overrides = readOverrides(id);
  const lines = txt.split(/\r?\n/);
  const events = [];
  let i = 0;
  let week = '';
  for (const raw of lines) {
    const wk = raw.match(/^#\s*(WEEK\s*\d+.*)$/i);
    if (wk) { week = stripMd(wk[1]).replace(/\s*—.*$/, '').trim(); continue; }
    if (!raw.trim().startsWith('|')) continue;
    const cells = raw.split('|').map(c => c.trim());
    // find a YYYY-MM-DD in the row (usually 2nd data cell)
    const joined = raw;
    const dm = joined.match(/(\d{4}-\d{2}-\d{2})/);
    if (!dm) continue;
    if (/^-+$/.test(cells.join(''))) continue; // separator
    // cells: ['', Day, Date, Platform, Format, Topic, Goal, Trending, Visual, Caption, '']
    const data = cells.filter((c, idx) => idx !== 0 || c !== '');
    // Robust index: locate the date cell, then read relative
    const dateIdx = cells.findIndex(c => /\d{4}-\d{2}-\d{2}/.test(c));
    const date = dm[1];
    const platformCell = cells[dateIdx + 1] || '';
    const platform = platformOf(platformCell);
    const format = stripMd(cells[dateIdx + 2] || '');
    const topic = stripMd(cells[dateIdx + 3] || '');
    const goal = stripMd(cells[dateIdx + 4] || '');
    const visual = stripMd(cells[dateIdx + 6] || '');
    const caption = stripMd(cells[dateIdx + 7] || '');
    const evId = `${id}-${i++}`;
    let title = topic || format || platform;
    events.push({
      id: evId,
      title: title,
      start: overrides[evId] || date,
      origDate: date,
      moved: !!overrides[evId] && overrides[evId] !== date,
      platform, format, topic, goal, visual, caption, week,
      color: PLATFORM_COLORS[platform] || PLATFORM_COLORS.default,
    });
  }
  return events;
}

// ---------- HTTP ----------
const MIME = {
  '.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8',
  '.json':'application/json; charset=utf-8','.md':'text/markdown; charset=utf-8','.txt':'text/plain; charset=utf-8',
  '.jpg':'image/jpeg','.jpeg':'image/jpeg','.png':'image/png','.gif':'image/gif','.webp':'image/webp',
  '.svg':'image/svg+xml','.mp4':'video/mp4','.mov':'video/quicktime','.webm':'video/webm','.m4v':'video/mp4',
  '.pdf':'application/pdf','.mp3':'audio/mpeg',
};
function send(res, code, body, type = 'application/json; charset=utf-8') {
  res.writeHead(code, { 'Content-Type': type, 'Cache-Control': 'no-store' });
  res.end(body);
}

const server = http.createServer((req, res) => {
  const parsed = url.parse(req.url, true);
  let pathname = decodeURIComponent(parsed.pathname);

  if (pathname === '/api/clients') return send(res, 200, JSON.stringify(listClients()));

  if (pathname.startsWith('/api/client/')) {
    const id = pathname.slice('/api/client/'.length);
    const detail = clientDetail(id);
    return detail ? send(res, 200, JSON.stringify(detail)) : send(res, 404, '{"error":"not found"}');
  }

  if (pathname.startsWith('/api/schedule/')) {
    const id = pathname.slice('/api/schedule/'.length);
    if (req.method === 'POST') {
      let body = '';
      req.on('data', c => { body += c; if (body.length > 1e6) req.destroy(); });
      req.on('end', () => {
        try {
          const { eventId, date } = JSON.parse(body || '{}');
          if (!eventId || !date) return send(res, 400, '{"error":"missing"}');
          writeOverride(id, eventId, date);
          return send(res, 200, '{"ok":true}');
        } catch { return send(res, 400, '{"error":"bad json"}'); }
      });
      return;
    }
    return send(res, 200, JSON.stringify(parseCalendar(id)));
  }

  if (pathname.startsWith('/raw/')) {
    const rest = pathname.slice('/raw/'.length);
    const slash = rest.indexOf('/');
    const id = slash === -1 ? rest : rest.slice(0, slash);
    const relPath = slash === -1 ? '' : rest.slice(slash + 1);
    const abs = safeJoin(path.join(CLIENTS_DIR, id), relPath);
    if (!abs || !fs.existsSync(abs) || fs.statSync(abs).isDirectory()) return send(res, 404, 'Not found', 'text/plain');
    const ext = path.extname(abs).toLowerCase();
    res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream', 'Cache-Control': 'no-store' });
    return fs.createReadStream(abs).pipe(res);
  }

  if (pathname === '/' || pathname === '/index.html') {
    return send(res, 200, fs.readFileSync(path.join(__dirname, 'index.html')), 'text/html; charset=utf-8');
  }
  send(res, 404, 'Not found', 'text/plain');
});

server.listen(PORT, () => {
  console.log(`\n  Agency — Agency Dashboard`);
  console.log(`  Running at  http://localhost:${PORT}\n`);
});
