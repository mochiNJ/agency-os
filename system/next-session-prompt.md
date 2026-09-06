# Next Session — start here

**State:** fresh install. No clients, no work in motion, no history.

**Before anything else, prove the machine works:**
1. `python system/structure-check.py` exits 0
2. `python system/sync.py` exits 0
3. Confirm the secrets exist locally: `.mcp.json`, `infra/fal/.env` (only if this machine generates
   images or video), `infra/postiz/.env` (only if this machine publishes). None of them are in git.

**Then:** onboard the first client with `system/new-client-workflow.md`, gate by gate. Park, never skip.
