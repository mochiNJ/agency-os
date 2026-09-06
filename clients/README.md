# `clients/`

**One folder per client, all with exactly the same shape. No exceptions.**

There are no clients yet. To add the first one:

```bash
python system/structure-check.py --new-client acme
```

That scaffolds the folder from `templates/client-folder-structure.md`. Then run the gated SOP in
`system/new-client-workflow.md` from G0. Each gate is locked by the previous gate's proof file:
park a gate if you must, never skip one.

The shape every client folder takes, and the law about where a file lives and when it dies, is
`system/file-system-law.md`. Check compliance with `python system/structure-check.py`.
