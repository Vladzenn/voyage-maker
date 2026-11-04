# Glowhaven standalone map brief

The author requested a PDF that can go to another image-generation chat with no old map artwork. This is documentation only; it neither changes nor imports world data and does not generate new map art.

`build.py` reads the current canonical world, selects the twenty Glowhaven regions and all eighty-two assigned locations, and combines those facts with `landmarks.txt`. The latter is an explicit exterior interpretation, including grouping and scale cautions. The script never reads or downloads an image. Regions use the source 5-by-4 grid and north-positive coordinates; master anchors are percentages from the left and top.

```sh
python tools/map-brief/build.py
```

Requires ReportLab and pypdf, available in the desktop bundled Python runtime. Windows uses Segoe UI; other environments use ReportLab's bundled Vera fonts. The PDF goes to `output/pdf/Glowhaven - Fresh Map Brief.pdf`, with a shared copy, editable Markdown and full-precision CSV under `world-draft/authoring/plans/`. PDF bookmarks provide region navigation.

The build asserts exact catalogue coverage, verifies all location/region names appear in extracted PDF text, counts embedded images and confirms the source world is unchanged. `review.json` records the source hash, all locations, anchors and section pages. It is not proof of a generated map's geometry or engine behavior.

The 5 November delivery was rendered with Poppler. All 28 pages were reviewed in a contact sheet; pages 3, 14 and 28 were also inspected at readable size. A pdfplumber bounds check found no text outside the safe margins. No old artwork was opened, embedded or linked. The document includes a single community coordinate-reference link; building-size ranges and unspecified exterior finishes are expressly art direction.

No public game patch notes are needed: the canonical world remains byte-identical to the Rebirth delivery.
