# 📲 Auto-Posting to Social Media — Plain-English Guide

*How the automated Instagram (and soon Facebook) posting works, why it works, and exactly what
happens next time. Written for a complete beginner. Last updated: 2026-07-25 (session 21).*

---

## 1. The one-paragraph version

Your videos live on **your own computer** inside a free tool called **Postiz** (think of it as your
private "schedule-and-post" control panel). Instagram won't let a computer just *hand* it a video —
instead, **Instagram reaches out and downloads the video itself** from a web address. The problem we
solved: your computer had no public web address, so Instagram couldn't reach it. We gave it one
(a secure tunnel to your own domain). Now Postiz can post to Instagram automatically. The **one catch**
we learned: the video file must be **small (~25 MB or less)**, or Instagram gives up while downloading.

---

## 2. The pieces (and a kitchen analogy)

| Piece | What it is | Analogy |
|---|---|---|
| **Postiz** | Free app on your PC that posts to social media | The **kitchen** where the meal (post) is plated |
| **The video** | Your approved reel (`.mp4`) | The **meal** |
| **Cloudflare Tunnel** | A secure public web address for your PC (`postiz.example.com`) | The **delivery hatch** the courier can reach |
| **Instagram/Meta** | Downloads the video from that address, then publishes | The **courier** who picks up the meal |
| **Publisher (Agent 14)** | The AI worker that tells Postiz "post this now" | The **waiter** who sends the order |

**Why the tunnel matters:** without it, the delivery hatch was inside a locked building
(`localhost` = "only this computer"). The courier (Instagram) couldn't find it. The tunnel is a
labelled public door the courier can actually walk up to — and it's locked/secure (HTTPS), so only
the right traffic gets through.

---

## 3. What has to be true before any post

1. **Docker is running** and **Postiz is up** — check: `docker ps` shows the `postiz` container; opening
   `http://localhost:5000` should redirect (status 307). If it errors (502), run:
   ```bash
   docker exec postiz pm2 restart backend
   ```
2. **The tunnel is running** — it's now a **Windows service** that starts automatically with your PC.
   Check: in PowerShell, `Get-Service cloudflared` shows **Running**. Nothing to open or babysit.
3. **The video is light — ≤ ~25 MB.** This is the golden rule. (See §5.)

---

## 4. How a post actually happens — the flow

```
Approved video (.mp4)
      │
      ▼
[If large] compress to a light copy  ── ffmpeg, ~25 MB, looks identical
      │
      ▼
Upload to Postiz  ──►  gets a PUBLIC address (https://postiz.example.com/uploads/…)
      │
      ▼
PROVE it: fetch that address from the internet → must return the video (200 OK)
      │
      ▼
Publisher (Agent 14) tells Postiz: "post this as a Reel, now, this caption, original audio"
      │
      ▼
Instagram downloads the video from the public address → publishes it
      │
      ▼
VERIFY on the real @client profile (not just Postiz — Postiz sometimes lies)
```

---

## 5. 🟡 THE GOLDEN RULE: keep the video small (~25 MB or less)

Instagram downloads the video *itself* through your home internet. Your home connection uploads
**slowly** (~1 MB per second), so a big file takes too long and Instagram **times out** (error 2207077
"Instagram Video download failed").

- A **70 MB** master took ~50 seconds → **failed.**
- A **25 MB** copy took ~18–35 seconds → **published fine.**

Instagram **re-compresses every video anyway**, so a smaller file looks *identical* once it's live.
We keep the big original ("master") untouched and post a light copy. The command:

```bash
ffmpeg -y -i INPUT.mp4 -c:v libx264 -profile:v high -pix_fmt yuv420p -preset slow -crf 21 \
  -c:a aac -b:a 128k -movflags +faststart OUTPUT-light.mp4
```

(`-crf 21` = high quality; raise to `23–25` for an even smaller file. `+faststart` lets Instagram
start reading immediately.)

---

## 6. 👉 Example: how it'll go next time (word-for-word)

Say next week you approve a **new reel about a 3D-printed cedar tree**, and the file is 60 MB.

> **You say:** *"Post the cedar reel to Instagram."*
>
> **What I (the AI) do, one step at a time:**
> 1. *"First let me make sure everything's awake."* — I check Docker, Postiz, and the tunnel service. If
>    the Postiz backend is asleep, I restart it (~40 seconds).
> 2. *"The file is 60 MB — too heavy for Instagram to download. I'll make a light 25 MB copy that looks
>    identical. Your original stays untouched."* — I run the ffmpeg command and show you two frames to
>    confirm quality.
> 3. *"Uploading it to Postiz now… done — here's its public web address."* — I upload and get the URL.
> 4. *"Let me prove Instagram can reach it before we post."* — I fetch the URL from the open internet;
>    it returns the video. ✅
> 5. *"Ready. I'll post it as a normal Reel, with your caption, original audio. This goes live publicly —
>    confirm?"* — you say yes.
> 6. I spawn the **Publisher agent**, which tells Postiz to post it now.
> 7. *"Instagram is downloading and processing it (~1–2 min)…"* — I wait, then **open your real profile**
>    and confirm the new reel is actually there, and give you the link.
> 8. **Two things only your phone can do:** pin the first comment, and add the location tag — **"Lebanon" only, never the town** (PUBLIC LOCATION RULE, brand-profile.md).
>    I remind you and you tap those in.

That's it. Your part is: **say "post it," approve the go-live, and do 2 taps on your phone.** I do the rest.

---

## 7. What's still manual (and why)

| Task | Why it's manual |
|---|---|
| **Pin the first comment** (`شو منطبع بعدها؟ / what should we print next?`) | Instagram's connection type exposes no comment/pin tool to Postiz. |
| **Add the geotag** ("Lebanon" only — never the town) | Same — no location tool over the connection. |
| **git push** | Saving to GitHub needs your login (security gate). I commit; you push. |
| **Approving a go-live** | Publishing is public and hard to undo — I always confirm with you first. |

---

## 8. Quick troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Postiz page shows **502** | Backend asleep after a restart | `docker exec postiz pm2 restart backend`, wait ~40s |
| Post shows **ERROR / "download failed" (2207077)** | Video too big | Compress to ≤25 MB and re-post |
| Postiz says **QUEUE/ERROR but it's actually live** | Known Postiz bug (#1562) | Trust the **Instagram profile**, not Postiz |
| Public URL won't load | Tunnel service stopped | `Get-Service cloudflared`; start it, or check Docker/Postiz are up |
| Nothing seems to reach Instagram | Wrong media address (localhost) | Media path must start with `https://postiz.example.com/uploads/…` |

---

## 9. The technical bits (for reference)

- **Tunnel:** named tunnel `postiz-a client` → `postiz.example.com` → `localhost:5000`. Runs as the
  Windows service `cloudflared` (Automatic start). Config: `C:\Users\kjn\.cloudflared\config.yml`.
- **Postiz addresses:** `MAIN_URL`/`FRONTEND_URL`/`NEXT_PUBLIC_BACKEND_URL` = `https://postiz.example.com`
  in `infra/postiz/docker-compose.yml`. Storage stays `local` (tunnel makes it public — no paid R2, no card).
- **Upload:** via `POST https://postiz.example.com/api/public/v1/upload` with a .NET multipart client
  (the Postiz MCP's own upload tool is broken on Windows). The `create_post` call needs `shortLink:false`
  and `tags:[]` or Postiz rejects it.
- **Connected account:** Instagram `@client`, integration id `cmrz80zop0001mm7e3s6aq6a0`.
- Full backstory + gotchas: memory `project_postiz_instagram_localhost`, and the session-21 changelog entry.

---

## 10. Who runs this — the Publisher agent

The agent responsible for posting is **Agent 14 — Publisher** (`.claude/agents/14-publisher.md`). It only
posts from the `approved/` folder, checks the QC stamp first, and confirms with you before the first post.
**As of session 21 it is FULL-AUTO for Instagram:** its spec now includes the complete workflow — preflight
health checks, **auto-compressing any video over ~25 MB**, the public-API upload, proving Meta can reach the
URL, posting a normal Reel, and **verifying on the real profile** (not trusting Postiz's status). You just
approve the go-live and do the 2 manual phone taps (pin comment + geotag).

---

## 11. Adding more platforms — Facebook, TikTok, YouTube

Good news: **the hard part is already built.** The tunnel, the public media URL, the ≤25 MB rule, and the
Publisher agent all work the same for every platform — because Facebook, TikTok, and YouTube also
**download the video themselves** from the same public address. So once an account is *connected*, posting
to it is the identical one-click flow.

**The only new work per platform is a one-time CONNECTION inside Postiz** (Postiz → *Add channel* →
pick the platform → log in → Authorize/Allow). Most platforms also require a small **developer app**
behind the scenes (like the Meta app we built for Instagram). Roadmap, easiest first:

| Platform | What's needed | Status |
|---|---|---|
| **Facebook** | Create the client Facebook **Page** first, then connect it in Postiz. The Meta app already exists. Caption already approved. | Queued (next up) |
| **TikTok** | Connect TikTok in Postiz (TikTok login + Authorize). ⚠️ An *unaudited* TikTok app may only post privately until TikTok approves it — verify the current flow first. | Not started |
| **YouTube (Shorts)** | Connect YouTube in Postiz (Google login + Allow). Needs a Google Cloud OAuth app; *unverified* apps are limited to test users until Google verifies — verify first. | Not started |

**Hard rule:** never state a platform's exact connect steps without loading Postiz's real "Add channel"
screen first — each platform's developer-app rules change. Research the current Postiz flow for that
platform, do the human-gated login/authorize with you, then verify the first post on the real profile.
Once connected, the **same Publisher agent** posts to it (it already has per-platform format rules for FB,
TikTok, LinkedIn, and X). Full step-by-step plan lives in `system/next-session-prompt.md` §(B).
