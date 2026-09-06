# 📐 THE FILE SYSTEM LAW

> **This is the single source of truth for where every file lives, what its status is, and when it dies.**
> Written 2026-09-06 after an audit found 36 groups of byte-identical duplicate images (40 MB), 227 files
> carrying status words in their names, 7 different names for "old stuff", and 4 clients with 4 different
> folder shapes. Enforced by `python system/structure-check.py`. Naming and drop-path detail that used to
> live in `system/asset-organization.md` is now here.

---

## WHY THE OLD SYSTEM FAILED (read this once, it explains every rule below)

Three failures, and only the third was really about tidiness.

**1. The pipeline copied instead of moving.** `pending-qc/` was designed as a *queue*. It ended up holding
23 files that had all been finished weeks earlier, because approving a file copied it to `approved/` and
left the original behind. A queue that is never drained becomes a log, and every slide then exists twice.
It also quietly burns the usage limit: "run QC on all pending-qc" re-scores two dozen finished files.

**2. Nothing said when a file dies.** Every rule we had was about creating and enforcing. Not one sentence
said when a file stops existing. So nothing ever did, and folders only grew.

**3. Status was written in three places that disagreed.** The folder said one thing, the filename suffix
(`-FINAL`, `-SUPERSEDED-2026-09-04`, `-v2`) said another, the date prefix said a third. The worst real case:
`slide-08-brandboard-v6.png` existed in `rejected/` and in `approved/` at the same time. There was no way to
answer "what IS slide 8?" without asking the user.

---

## LAW 1 — IN MOTION vs AT REST

Every working file is in exactly one of two states, and the folder says which.

| | `pipeline/` | `library/` |
|---|---|---|
| Means | in motion, being worked on | at rest, finished |
| Lifetime | days | permanent |
| Must be empty when a job closes | **yes** | never empty |
| Grouped by | stage | **post** |

`pipeline/` is a set of queues. **A queue that is not empty at the end of a job is a bug**, and
`structure-check.py` reports it. If a file is still sitting in `pipeline/` after a job closed, either the job
did not really close or the file should have been deleted.

`library/posts/` is the only home of finished work, and it is grouped **by post, not by stage**. One post is
one folder holding its slides, its caption, and its manifest. This is what kills "the same picture in five
different files": there is exactly one folder where slide 8 lives, and it sits next to the caption it ships
with.

---

## LAW 2 — WRONG IS DELETED, DIFFERENT IS KEPT

**This is the user's own rule, from how he manages photos on his phone, and it is the rule that keeps
folders permanently small.** Every rejection has exactly one of two reasons, and the reason decides the fate.

### WRONG → delete it, now, without asking

The product is inaccurate, the wordmark is garbled, the palette is retired, the text is broken, the logo is
wrong. **It can never be posted, so it has no future.** Keeping it costs storage, costs attention, and is
actively dangerous: a wrong asset with a neutral name gets picked up and used by a later agent.

Delete it for real. **Git history holds every deleted document and image forever**, so nothing is ever
truly lost and it can be recovered on request. That safety net is exactly why deleting is the correct
default and not a risk.

> ### ⚠️ THE ONE EXCEPTION: VIDEO HAS NO SAFETY NET
> **`*.mp4`, `*.mov`, `*.avi` and `*.mkv` are in `.gitignore`, so video is NOT in git history.**
> Deleting a video is permanent and unrecoverable. The whole "delete freely, git has it" argument does
> not apply to video, and a `.mp3` soundtrack is only in git if it was force-added.
>
> **So: never delete a video.** A video that is wrong goes to `_alts/` with the reason in its name, and
> you tell the user it is there. If disk space ever genuinely forces the issue, ask first.
> (Found 2026-09-06: 25 video files were sitting on disk with zero git coverage.)

### DIFFERENT → keep it in `_alts/`

The asset is *correct* but takes a creative direction we did not choose. That is not a failure, it is a real
option for a future post. Keep it in the nearest `_alts/` folder with a name that says what the direction was
(`hero-warm-daylight`, not `hero-v2`).

### The test, when it is not obvious

> Could this file ever be posted, exactly as it is, to a real audience?
> **No** to wrong facts or broken craft, delete. **Yes but we preferred another**, `_alts/`.

`_alts/` lives as long as the product does. When a product is retired, its alternates go with it.

### The three places work can live, and how to tell them apart

This is the question that confuses everyone, so answer it with the test in the last column.

| | holds | lifetime | **the test** |
|---|---|---|---|
| `products/[product]/` | everything about **a thing you sell**: its identity, its real photos, its locked hero, its generated scenes | as long as the product exists | *"Would this still matter if we never posted again?"* **Yes** → product. |
| `library/posts/[date-slug]/` | **one finished post**: its slides, its caption, its manifest | forever, it is a record of what we made | *"Is this a specific thing that goes out on a specific day?"* **Yes** → post. |
| `campaigns/[name]/` | a **time-boxed programme across several posts and channels**: the brief, the budget, the ad copy, the email sequence, and LINKS to its posts | the run of the campaign | *"Does this coordinate several posts plus at least one non-social channel?"* **Yes** → campaign. |

**A campaign never holds product identity, and never holds the post files themselves.** It holds the plan
and points at both. Getting this wrong is what put the demo brand's logo, wordmark, palette board and brand lock
under `campaigns/` for a month, where nobody looking at the product would ever find them (fixed 2026-09-06).

**If you are unsure between product and campaign, it is the product.** Most work is.

### Inspiration lives OUTSIDE the clients, in one library

`inspiration-library/` is the **only** home for reference material. There is no
`clients/*/inspiration/`, and creating one is a violation.

> **The user, 2026-09-06:** *"this one should be outside in the AI agency, not in the agency, because those
> inspirations will be useful for us, for all our clients, and they need to be organized by type of
> business."*

He is right, and the evidence agreed with him: the per-client board that existed was a hollow 31-line
shell restating a 197-line type board, so it added a second place to look and nothing else. Inspiration is
**reusable technique**, not the property of one client. A move we learn from a coffee brand should be
available to a jewellery brand. Splitting it per client fragments it and guarantees duplication.

**Golden rule, unchanged: steal the technique, adapt it to THIS client and product, never clone the source.**

---

## LAW 5 — A STATUS FILE SAYS WHAT IS TRUE NOW. IT IS NEVER APPENDED TO.

This is LAW 1 applied to documents, and it is the same bug in a different costume.

A file whose job is to answer *"where are we?"* must be **edited in place**. The moment someone appends a
new dated block instead of rewriting the row, it stops being a status and becomes a log, and then nobody
can tell what is currently true without reading the whole thing.

It had already happened twice, badly, before 2026-09-06:

| file | what it became | now |
|---|---|---|
| `system/pipeline-status.md` | **618 lines, 63 stacked dated blocks** | 47 lines, a table |
| `system/next-session-prompt.md` | **1135 lines, 21 stacked handoffs**, only the top one live, titled for a client session weeks old | 102 lines, one handoff |

**Where things go instead:**

| this | goes here |
|---|---|
| what is true right now | the status file, **edited in place** |
| what changed and why | `system/changelog.md` (append-only) |
| the session narrative | `system/progress.md` (append-only) |
| a fact proven once, never to be re-derived | `system/verified-facts.md` (append-only) |

`structure-check.py` holds a line cap per status file and fails when one is exceeded. If a cap is genuinely
too tight, raise it deliberately in the checker and say why. Do not quietly let the file grow.

---

## LAW 3 — THE FOLDER IS THE STATUS. THE NAME NEVER SAYS STATUS.

A file's status is **where it is**, never what it is called. Status changes by **moving**, never by copying.

**Banned in every filename**, forever:
`FINAL`, `OLD`, `NEW`, `SUPERSEDED`, `APPROVED`, `REJECTED`, `RETIRED`, `DRAFT`, `TEMP`,
`copy`, `untitled`, `v2`/`v3` used as a status, `-1`/`(1)` duplicate suffixes.

Why: two files called `slide-04-palette-FINAL.png` with different dates is not a version history, it is an
unanswerable question. If you need to know what came before, that is what git is for.

**Names describe content**: `slide-04-palette.png`, `world-04-dark-wet-stone-night.png`,
`hero-warm-daylight.png`.

### Naming conventions

- **lowercase-with-hyphens. No spaces, ever.** A space breaks shell paths, scripts and the link checker.
- **Describe the content, not the origin.** Never `file_00000000abd88246.png`, never `chatgpt-output.png`.
- **Zero-pad numbered sets** so they sort: `slide-01`, `world-02`.
- **Date-prefix things that are a point in time** (`YYYY-MM-DD-`): job tickets, prompts, reports, posts.
- **A file in `_alts/` says what direction it is**, not what number it is.

---

## LAW 4 — TWO UNDERSCORE FOLDERS EXIST. NO OTHERS.

The audit found seven names all meaning "not current": `_archive`, `_superseded`, `_retired`, `_drafts`,
`_rejected`, `rejected`, `_raw`. Seven names for one idea means nobody knows which to use, so people invent
an eighth. From now on there are **two**, and `structure-check.py` fails on any other.

| Folder | Means | Who empties it |
|---|---|---|
| `_inbox/` | things that have just arrived and are not filed yet | Claude, same turn, always |
| `_alts/` | correct work we did not choose (LAW 2) | nobody, until the product retires |

**There is no `_archive/`. Git is the archive.** An archive folder is just a second copy of the repo that
nobody prunes. Anything worth keeping is either live, an alternate, or in history.

*Exception, and only this one:* `system/jobs/`, `system/qc-log.md`, `system/changelog.md`,
`system/progress.md`, `clients/*/prompts/` and each client's `creative-decisions-log.md` are **append-only
history**. They record what was true at the time and are never rewritten or pruned, even when the paths
inside them go stale. Do not "fix" a job ticket to match a new structure.

---

## THE CANONICAL CLIENT SHAPE

Every client, real or demo, has this shape. No client invents its own.

```
clients/[client]/
├── README.md                  the index: who they are, what stage, what is live, where things are
│
├── brand-profile.md           THE BRAIN FILES. Single source of truth for identity and knowledge.
├── competitor-report.md       Never duplicated into another file (RULE A: point, don't copy).
├── trend-report.md
├── seo-aeo-report.md
├── content-calendar.md
├── creative-decisions-log.md  append-only: every test, result and piece of user feedback
│
├── brand/                     the CLIENT's own identity assets
│   ├── logo/                  the real logo files. Never re-typeset by hand.
│   └── brand-lock.md          strict palette/font/name lock, where a client has one
│
├── products/[product]/        ONE folder per product. Mandatory before production starts.
│   ├── product.md             every known fact. Anything not here is UNKNOWN and is never stated publicly.
│   ├── brand-lock.md          this product's OWN locked palette/type, if it has one
│   ├── _inbox/                WHERE THE USER DROPS FILES. Normally empty.
│   ├── brand/                 THIS PRODUCT's identity. A demo house is its own brand: its
│   │                          wordmark, palette board, logo. Never the agency's or client's.
│   ├── source-photos/         real photography supplied by the client. Never regenerated.
│   ├── hero/                  the LOCKED reference image. Everything else is built from this.
│   ├── worlds/                scene and environment shots
│   └── _alts/                 correct, not chosen
│
├── pipeline/                  IN MOTION. Drains to empty at the end of every job.
│   ├── _inbox/
│   ├── pending-humanizer/
│   ├── pending-qc/
│   └── pending-signoff/       passed QC, waiting on the client. QC is not sign-off.
│
├── library/                   AT REST. The only home of finished work.
│   └── posts/YYYY-MM-DD-slug/
│       ├── post.md            the manifest: caption, on-slide copy, QC score, sign-off, where it went live
│       ├── slide-01.png ...
│       └── _alts/
│
├── campaigns/[campaign]/      multi-post programmes
├── prompts/                   append-only: every image and video prompt, verbatim
├── qc-notes/                  append-only: QC verdicts and the lessons in them
└── reports/                   monthly analyst output
```

**Never build a new client's folders by hand.** That is how we ended up with four clients in four
different shapes. Run:

```bash
python system/structure-check.py --new-client acme-widgets
```

then work through the gated SOP in `system/new-client-workflow.md`.

**`uploads/` and `assets/` no longer exist.** They overlapped (`products/[product]/source-photos/` vs
`assets/images/`) and neither said whether a file was raw, chosen, or dead. Client-supplied photography is
`products/[product]/source-photos/`, identity is `brand/`, everything else is a product or a post.

---

## THE ROUTING RULE — where does a new file go?

Walk it in order. Stop at the first answer.

0. **Is it reference material we admire and want to learn from?** (a screenshot, a saved reel, a board)
   → `inspiration-library/`. **Never inside a client.** Stop here.

1. **Is it about ONE client?**
   No, and it is about *how the agency runs* → `system/`.
   No, and it is *reference for a human to read* → `docs/`.
   No, and it is a *reusable starting point* → `templates/`.
   Yes → continue.

2. **Is it the CLIENT's own identity?** (their logo, their palette lock, their font)
   → `clients/[client]/brand/`

3. **Is it knowledge?** (research, decisions, calendar, profile) → a brain file at the client root.

4. **Is it about one product?** → `clients/[client]/products/[product]/`, into the sub-folder that matches
   what it is: `product.md` (facts), `brand/` (that product's OWN wordmark and palette),
   `source-photos/` (real photography), `hero/` (the locked reference), `worlds/` (generated scenes),
   `_alts/` (correct but not chosen).

5. **Is it work in motion?** → `pipeline/`, in the queue for the stage it is waiting on.

6. **Is it finished and shippable?** → `library/posts/YYYY-MM-DD-slug/`

6b. **Does it coordinate several posts AND a non-social channel** (ads, email, influencer)?
   → `campaigns/[name]/`, holding the brief and the cross-channel pieces, LINKING to its posts.
   If you are hesitating between this and a product, **it is the product**.

7. **Does nothing fit?** Then and only then, **create a folder**, and in the SAME turn:
   - give it a one-line charter at the top of its own `README.md` (what belongs here, what does not),
   - register it in `system/folder-registry.md`,
   - add it to `PROJECT-MAP.md`,
   - run `python system/structure-check.py` to confirm it is legal.

   A folder that is not registered is a folder nobody else will ever find. `structure-check.py` reports
   unregistered folders, so this cannot be skipped quietly.

---

## THE USER NEVER FILES ANYTHING

> **STANDING RULE (user, 2026-09-05):** *"Whenever I add things myself, I want you to change their name to
> the more logical one, put them in the right place, etcetera. I don't need to tell you this."*

When the user drops files anywhere, filing them is Claude's job and happens **automatically, in the same
turn, without being asked.** This is dispatcher work (file organization is an explicit CLAUDE.md exception),
so do it inline, never spawn an agent for it.

1. **LOOK at every file** before naming it. Open the images. Never name a file from its position in a list or
   from what the user said it probably is. The name must describe what the file actually contains.
2. **APPLY LAW 2 while looking.** Wrong goes now. Do not file garbage tidily.
3. **RENAME** by the conventions above.
4. **MOVE** it to the folder the routing rule gives, creating it if needed.
5. **DELETE the empty drop folder** the user created.
6. **UPDATE every path that pointed at the old location**, `system/facts.json` first, then any doc.
7. **RUN** `python system/sync.py` and `python system/structure-check.py`. Both must pass.
8. **INDEX it** in that folder's `README.md`, one line per file, so the next agent can pick the right file
   without opening ten images.
9. **REPORT** what you did, in one short list.

### Always give the drop path

> **STANDING RULE (user, 2026-09-05):** *"Always tell me, give me the path where I should put the picture.
> I will put it for you, and then you rename it yourself."*

Whenever you ask the user to supply or generate anything, **state the exact folder path in plain text he can
copy.** It is always an `_inbox/`. Same folder every time, so he never has to think about it. He drops it
under whatever name it came with; naming and filing are yours.

---

## WHY THIS MATTERS MORE THAN IT LOOKS

Sub-agents spawn with **no memory**. They find assets by reading a path in a file. So an unfiled, unnamed,
unindexed image is invisible to the entire pipeline, and the agent regenerates something we already own,
burning the usage limit on a file already sitting on disk.

A wrong asset that was kept "just in case" is worse than a missing one, because an agent will eventually use
it. That is the real argument for LAW 2, and it is why deleting is the safe choice, not the reckless one.

---

## ENFORCEMENT

A rule only bites where it is forced. This law is forced in three places:

1. **`python system/structure-check.py`** fails on:
   - status words or version stamps in filenames, spaces or uppercase in paths
   - any underscore folder other than `_inbox`/`_alts`, and any graveyard folder
   - byte-identical duplicate media
   - stale files left in a `pipeline/` queue
   - a client folder **not registered in `system/active-clients.md`** *(added after a scaffold test,
     "acme-widgets", was left behind and no check caught it because "an extra client" was
     structurally legal)*
   - any `clients/*/inspiration/` *(reference material lives in `inspiration-library/`)*
   - empty folders, placeholder-only folders, and a `.gitkeep` that has become a **directory**
     *(a real bug produced by a bad move during the 2026-09-06 migration)*
   - a **governed folder with no `README.md` charter**
   - a **status file that has grown into a log** (see LAW 5)
   - an **agent file** missing `model: sonnet`, a CONTRACT block, the skill-router pointer, or this law
   - a **skill folder with no loadable `SKILL.md`** at its top level
   - **a live document that points at an abolished folder**, written relatively (`slides/reveal.png`,
     `uploads/logo`). `sync.py` cannot see these, because it only validates paths that start with a
     top-level folder. **17 files were carrying them** after the restructure, including the gated
     onboarding SOP and three templates, which between them would have taught every FUTURE client the
     abolished structure.
   - **code that reads an abolished folder.** `sync.py` only link-checks `.md`, so
     `dashboard/server.js` silently kept reading `uploads/logo` and `content/approved` through the
     2026-09-06 restructure and rendered every client with no logo and no assets while both checkers
     reported clean. Code is scanned now, for slash paths *and* for quoted path segments, because the
     first version of this check matched only the former and therefore missed the exact bug it was
     written for.
2. **Agent 16 (quality-controller) hard-fails** any deliverable whose assets violate this law.
3. **The dispatcher runs both checkers** before reporting any filing work as done.

Run it any time:

```bash
python system/structure-check.py
```
