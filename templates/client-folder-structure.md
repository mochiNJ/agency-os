# Client folder structure

> **The canonical client shape is defined once, in
> [`system/file-system-law.md`](../system/file-system-law.md), and every folder's charter is in
> [`system/folder-registry.md`](../system/folder-registry.md).** This file used to restate the shape,
> which meant the two could disagree. It no longer does (RULE A: point, don't copy).

## Do not build a new client's folders by hand

```bash
python system/structure-check.py --new-client acme-widgets
```

That creates the full canonical shape with `_inbox/` drop points and stub brain files, then verifies it.
Building it by hand is how we ended up with four clients in four different shapes.

Afterwards, run the gated onboarding SOP in [`system/new-client-workflow.md`](../system/new-client-workflow.md),
which fills those files in the right order, each gate locked by the previous gate's proof.
