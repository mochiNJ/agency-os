# Postiz — self-hosted publisher (free forever)

Runs Postiz locally in Docker so the Publisher agent (Agent 14) can post to Instagram/TikTok
without a paid plan. UI at http://localhost:5000.

## Files
- `docker-compose.yml` — Postiz + Postgres + Redis. Committed (no secrets inside).
- `.env` — JWT secret, DB password, Instagram app keys. **Gitignored — never committed.**

## Setup order (a human is needed only for installs, logins, and the Instagram authorization)
1. **Install Docker Desktop** (free for personal use). It sets up WSL2; needs a restart.
2. **Start Postiz:** from this folder run `docker compose up -d`, then open http://localhost:5000
   and create the first (local, admin) account.
3. **Instagram developer app (Meta):** create an app, enable Instagram, copy App ID + App Secret
   into `.env` (`INSTAGRAM_APP_ID`, `INSTAGRAM_APP_SECRET`), then `docker compose up -d` again to
   reload. Add your own IG account as an app tester (lets you post to your own account without
   Meta's full app review).
4. **Connect the channel** inside Postiz → Settings → Channels → Instagram, and authorize.
5. **Get the Postiz API key** (Settings → API) and put it in the project `.mcp.json` under the
   `postiz` server (`POSTIZ_API_KEY`). Restart Claude so the MCP connects.
6. The Publisher agent posts the approved reel.

## Handy commands (run from this folder)
- Start / reload:  `docker compose up -d`
- Stop:            `docker compose down`
- View logs:       `docker compose logs -f postiz`
- Update Postiz:   `docker compose pull && docker compose up -d`
