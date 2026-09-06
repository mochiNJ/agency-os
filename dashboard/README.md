# 📊 `dashboard/` — the agency dashboard

**Charter: our own internal view of the clients folder. Not a client deliverable.**

```bash
node dashboard/server.js      #  ->  http://localhost:4321
```

Dependency-free Node (`http`, `fs`, `path`, `url` only), so there is no `package.json` and nothing to
install. `start-dashboard.bat` is the one-click version.

## It READS the repo, so the repo's structure is its API

`server.js` walks `clients/` live. It reads:

| it shows | it reads |
|---|---|
| the client logo | `clients/<id>/brand/logo/` |
| the brain docs | the loose `.md` files at the client root |
| products | `clients/<id>/products/<product>/product.md` |
| assets | `brand/`, `products/`, `library/posts/` |

**`pipeline/` is deliberately excluded**: it holds work in motion, which must drain to empty, so anything
sitting there is a bug rather than something to display.

> ### ⚠️ If you move a folder, fix this file in the same turn
> On 2026-09-06 `uploads/`, `assets/` and `content/` were abolished and this server was **not** updated
> with them. It kept reading `uploads/logo` and `content/approved`, so every client silently rendered with
> **no logo and zero assets**, and no checker noticed, because `sync.py` only link-checks `.md` files.
> `structure-check.py` now scans code for abolished paths too. That gap is the reason this warning exists.

## The client list here is DISPLAY ONLY

`REGISTRY` in `server.js` holds colours and labels. **The source of truth for who is a client and what
state they are in is [`system/active-clients.md`](../system/active-clients.md).** That block had drifted:
[client] and [client] were missing entirely, and [client] was still marked a "test".
