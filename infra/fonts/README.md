# Vendored font files

Real font files for local text rendering, so slides can be set in a client's actual brand face rather than a
lookalike. All Google Fonts / OFL, cleared for commercial use.

**Never pick a font from this folder.** The client's `brand-profile.md` is the single source of truth for
which face to use. This folder only holds the files.

| File | Family | Used by |
|---|---|---|
| `DMSerifDisplay-Regular.ttf` | DM Serif Display | **the agency display.** Single weight by design. Never synthesise bold or italic on it, that is a QC hard-fail. Never set below 56px. |
| `Poppins-Regular.ttf` | Poppins 400 | the agency body |
| `Poppins-Medium.ttf` | Poppins 500 | the agency sub-head, fine print |
| `Poppins-SemiBold.ttf` | Poppins 600 | the agency tag / kicker, and the logo's own descriptor |
| `Poppins-Bold.ttf` | Poppins 700 | the agency dense-headline alternate |
| `Poppins-ExtraBold.ttf` | Poppins 800 | the agency long-line cover alternate, big numbers |

`_retired/` holds Sora and Inter, the agency's former fonts. Do not use them for the agency.

**Adding a client's font:** fetch it from its real source into this folder and add a row. Use the direct raw
file URL from the google/fonts repo. The `fonts.google.com/download?family=` endpoint returns an HTML page,
not a zip.
