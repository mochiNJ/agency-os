#!/usr/bin/env python3
"""Render a slide at the sizes people ACTUALLY see it, so text legibility is judged honestly.

Why: the 13 a demo house slides all passed QC while their body text was 8.8dp in the feed, which is
unreadable. They were judged at full 1080px zoom. Nobody looks at them that way.

Usage:
    python system/preview-at-real-size.py <image.png | folder>

Writes, next to the source, into a `_size-check/` folder:
    <name>-FEED.png   412px wide, how it looks when someone opens the post
    <name>-GRID.png   137px wide, how it looks in the profile grid

Then LOOK at those two files. If the cover headline cannot be read in the GRID render, the post will
not get tapped. See system/text-size-rules.md for the hard minimums.
"""
import os
import sys

from PIL import Image

FEED_W = 412   # a post opened in the feed, on a ~412dp-wide phone
GRID_W = 137   # one tile of the 3-across profile grid


def preview(path, outdir):
    im = Image.open(path).convert("RGB")
    base = os.path.splitext(os.path.basename(path))[0]
    made = []
    for label, w in (("FEED", FEED_W), ("GRID", GRID_W)):
        h = max(1, round(im.height * w / im.width))
        out = os.path.join(outdir, "%s-%s.png" % (base, label))
        im.resize((w, h), Image.LANCZOS).save(out)
        made.append(out)
    return made


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    target = sys.argv[1]

    if os.path.isdir(target):
        files = [os.path.join(target, f) for f in sorted(os.listdir(target))
                 if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    else:
        files = [target]
    if not files:
        print("no images found in", target)
        return 1

    outdir = os.path.join(os.path.dirname(os.path.abspath(files[0])), "_size-check")
    os.makedirs(outdir, exist_ok=True)

    for f in files:
        for m in preview(f, outdir):
            print("wrote", os.path.relpath(m))

    print("\n%d slide(s) rendered at real viewing sizes -> %s" % (len(files), outdir))
    print("NOW LOOK AT THEM. Judge legibility there, never at full size.")
    print("Minimums: system/text-size-rules.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
