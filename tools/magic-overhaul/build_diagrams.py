"""Export the actual reaction catalogue as a vector PDF and high-resolution PNGs."""
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys
import zipfile

from PIL import Image, ImageOps, ImageDraw
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A3, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / 'output/pdf/Elemental Reactions'
ARCHIVE = ROOT / 'world-draft/authoring/plans/Elemental Reactions - Visual Reference'
TMP = ROOT / 'tmp/pdfs/elemental-reactions'
ROWS = json.loads((HERE / 'reactions.json').read_text(encoding='utf-8'))
W, H = landscape(A3)
INK = '#1e3042'
MUTED = '#5e6c79'
PAPER = '#faf8f2'
LINE = '#dce2e4'
GROUPS = [(20, 'Impact', '#a95d1e', '#fff0dc', 'Normal hit damage x 1.20, with a distinctive elemental clash.'),
          (10, 'Damage + disruption', '#7151a2', '#f1eafb', 'Normal hit damage x 1.10 plus a brief tactical penalty.'),
          (0, 'Control', '#167a77', '#e3f4ef', 'Normal hit damage x 1.00 plus the listed temporary effect. Zero bonus does not mean zero damage.')]
ELEMENTS = {
    'fire': '#c95338', 'water': '#297ea6', 'ice': '#5d9ea8', 'lightning': '#ad801a',
    'wind': '#478c86', 'earth': '#997047', 'metal': '#63778b', 'nature': '#58894a',
    'poison': '#8b9850', 'arcane': '#8963b5', 'void': '#4e526f', 'light': '#bc943d',
    'dark': '#65566e', 'gravity': '#5c6bb1', 'psychic': '#b85d8c', 'sound': '#b36e52',
}
FRIENDLY = {
    'Flashburst': 'Next footing-dependent defense: -3.',
    'Sprayveil': 'Next visually aimed attack: -3.',
    'Frostflower': 'Next movement-dependent check: -3.',
    'Burdenfall': 'Next grounded physical attack damage: -5%.',
    'Bellshock': 'Next attack damage with the affected metal implement: -5%.',
    'Prismwink': 'Next visually aimed check: -3.',
    'Nightshade': 'Next physical attack damage: -5%, in a susceptible living body.',
    'Hollow Echo': 'Next concentration check: -3, for an actual mind.',
    'Cinderbloom': 'Next physical attack damage: -10%, in a susceptible body.',
    'Rimebind': 'Next movement-dependent block or evade check: -5.',
    'Ironburr': 'Next attack damage with an existing metal weapon: -10%.',
    'Sparkstitch': 'Next damaging spell output: -10%.',
    'Bitterwake': 'Next visually aimed attack: -5, if eyes are susceptible.',
    'Echochatter': 'Next hearing- or concentration-dependent check: -5, for an actual mind.',
    'Nightweight': 'Next movement-dependent check: -5, for a grounded target.',
    'Afterglow': 'Next concealment-dependent defense or hiding check: -5. Target must already be perceived.',
}


def font_path(filename, fallback):
    p = Path('C:/Windows/Fonts') / filename
    return p if p.exists() else Path('/usr/share/fonts/truetype/dejavu') / fallback


pdfmetrics.registerFont(TTFont('Body', str(font_path('segoeui.ttf', 'DejaVuSans.ttf'))))
pdfmetrics.registerFont(TTFont('Bold', str(font_path('segoeuib.ttf', 'DejaVuSans-Bold.ttf'))))
pdfmetrics.registerFont(TTFont('Display', str(font_path('georgiab.ttf', 'DejaVuSerif-Bold.ttf'))))


def fill(color):
    C.setFillColor(colors.HexColor(color))


def stroke(color):
    C.setStrokeColor(colors.HexColor(color))


def text(x, top, s, size=12, font='Body', color=INK, align='left'):
    fill(color)
    C.setFont(font, size)
    f = C.drawString if align == 'left' else C.drawCentredString if align == 'center' else C.drawRightString
    f(x, H - top - size * .82, s)


def lines(x, top, s, width, size=12, leading=None, color=INK, font='Body', max_lines=10):
    leading = leading or size * 1.3
    out = []
    for para in s.split('\n'):
        line = ''
        for word in para.split():
            proposed = (line + ' ' + word).strip()
            if pdfmetrics.stringWidth(proposed, font, size) > width and line:
                out.append(line)
                line = word
            else:
                line = proposed
        out.append(line)
    assert len(out) <= max_lines, (s, out)
    for i, line in enumerate(out):
        assert pdfmetrics.stringWidth(line, font, size) <= width + .1, line
        text(x, top + i * leading, line, size, font, color)
    return len(out) * leading


def box(x, top, width, height, bg='#ffffff', border=LINE, radius=10):
    fill(bg)
    stroke(border)
    C.setLineWidth(.7)
    C.roundRect(x, H - top - height, width, height, radius, fill=1, stroke=1)


def rule(x1, t1, x2, t2, color=LINE, width=1):
    stroke(color)
    C.setLineWidth(width)
    C.line(x1, H - t1, x2, H - t2)


def arrow(x1, top, x2, color=MUTED, width=1.5):
    rule(x1, top, x2 - 5, top, color, width)
    fill(color)
    p = C.beginPath()
    p.moveTo(x2, H - top)
    p.lineTo(x2 - 7, H - top + 4)
    p.lineTo(x2 - 7, H - top - 4)
    p.close()
    C.drawPath(p, fill=1, stroke=0)


def element(name, x, top, radius=13, label=False):
    """Original vector symbols, avoiding missing color-emoji glyphs."""
    cy = H - top
    fill(ELEMENTS[name])
    C.circle(x, cy, radius, fill=1, stroke=0)
    C.saveState()
    C.translate(x, cy)
    C.scale(radius / 14, radius / 14)
    C.setStrokeColor(colors.white)
    C.setFillColor(colors.white)
    C.setLineWidth(1.25)
    p = C.beginPath()
    if name in ('fire', 'water'):
        p.moveTo(0, 9)
        p.curveTo(-2, 3, -8, -1, -6, -5)
        p.curveTo(-4, -10, 5, -10, 6, -4)
        p.curveTo(7, 1, 2, 5, 0, 9)
        C.drawPath(p, fill=0, stroke=1)
        if name == 'fire':
            C.line(-1, -6, 2, 0)
    elif name == 'lightning':
        for i, v in enumerate([(2, 9), (-5, 0), (0, 0), (-3, -9), (6, 2), (1, 2)]):
            (p.moveTo if i == 0 else p.lineTo)(*v)
        p.close()
        C.drawPath(p, fill=1, stroke=0)
    elif name in ('ice', 'light', 'arcane'):
        n = 6 if name == 'ice' else 8 if name == 'light' else 4
        for i in range(n):
            a = i * 2 * math.pi / n
            lo = 2.5 if name == 'light' else 0
            C.line(math.cos(a) * lo, math.sin(a) * lo, math.cos(a) * 8, math.sin(a) * 8)
        if name == 'light':
            C.circle(0, 0, 3, fill=0, stroke=1)
    elif name in ('dark', 'void', 'gravity'):
        C.circle(0, 0, 6.5, fill=0, stroke=1)
        if name == 'dark':
            p.moveTo(2, 6)
            p.curveTo(-7, 5, -6, -5, 2, -6)
            C.drawPath(p, stroke=1)
        elif name == 'void':
            C.circle(0, 0, 2.3, fill=1, stroke=0)
        else:
            C.ellipse(-10, -3, 10, 3, stroke=1)
            C.circle(0, 0, 1.8, fill=1, stroke=0)
    elif name == 'earth':
        p.moveTo(-9, -6)
        p.lineTo(-2, 6)
        p.lineTo(2, -1)
        p.lineTo(5, 4)
        p.lineTo(10, -6)
        p.close()
        C.drawPath(p, stroke=1)
    elif name == 'metal':
        for i in range(6):
            a = (i + .5) * math.pi / 3
            (p.moveTo if i == 0 else p.lineTo)(math.cos(a) * 8, math.sin(a) * 8)
        p.close()
        C.drawPath(p, stroke=1)
        C.circle(0, 0, 3, stroke=1)
    elif name == 'nature':
        p.moveTo(-7, -7)
        p.curveTo(-9, 3, 0, 9, 8, 7)
        p.curveTo(9, -2, 1, -9, -7, -7)
        C.drawPath(p, stroke=1)
        C.line(-7, -7, 5, 4)
    elif name == 'poison':
        p.moveTo(-3, 8)
        p.lineTo(3, 8)
        p.lineTo(3, 3)
        p.lineTo(7, -5)
        p.curveTo(9, -9, -9, -9, -7, -5)
        p.lineTo(-3, 3)
        p.close()
        C.drawPath(p, stroke=1)
        C.line(-5, -3, 5, -3)
    elif name == 'wind':
        for y, end in [(4, 7), (0, 10), (-4, 5)]:
            C.line(-9, y, end - 3, y)
            C.arc(end - 6, y, end, y + 5, 0, 220)
    elif name == 'sound':
        C.line(-3, -4, -3, 7)
        C.line(-3, 7, 5, 9)
        C.line(5, 9, 5, -2)
        C.ellipse(-8, -8, -2, -3, fill=1, stroke=0)
        C.ellipse(0, -6, 6, -1, fill=1, stroke=0)
    elif name == 'psychic':
        p.moveTo(-10, 0)
        p.curveTo(-3, 8, 3, 8, 10, 0)
        p.curveTo(3, -8, -3, -8, -10, 0)
        C.drawPath(p, stroke=1)
        C.circle(0, 0, 3, stroke=1)
    C.restoreState()
    if label:
        text(x, top + radius + 6, name.title(), 12, 'Bold', align='center')


def header(kicker, title, subtitle, page):
    fill(PAPER)
    C.rect(0, 0, W, H, fill=1, stroke=0)
    text(40, 27, 'THE SCHOOLS OF MAGIC, ARISE!', 10, 'Bold', '#6f6d60')
    text(W - 40, 27, kicker, 10, 'Bold', MUTED, 'right')
    text(40, 57, title, 33, 'Display')
    text(40, 103, subtitle, 12, color=MUTED)
    rule(40, H - 43, W - 40, H - 43)
    text(40, H - 31, 'Magic Overhaul | 6 November 2026 | Current design reference', 8.5, color=MUTED)
    text(W - 40, H - 31, f'{page} / 5', 8.5, color=MUTED, align='right')


def pair(x, top, a, b, radius=10, font=10):
    element(a, x + radius, top + radius, radius)
    text(x + 2 * radius + 6, top + radius - font / 2, a.title(), font, 'Bold')
    first = pdfmetrics.stringWidth(a.title(), 'Bold', font) + 2 * radius + 20
    text(x + first, top + radius - font / 2, '+', font + 1, color=MUTED)
    element(b, x + first + 26, top + radius, radius)
    text(x + first + 2 * radius + 32, top + radius - font / 2, b.title(), font, 'Bold')


def overview():
    header('ALL 24 COMBINATIONS', 'The elemental reaction atlas',
           'Either order works. Use separate landed hits on the same target, during the same or following turn.', 1)
    gap = 18
    cw = (W - 80 - 2 * gap) / 3
    for col, (bonus, title, accent, tint, _) in enumerate(GROUPS):
        x = 40 + col * (cw + gap)
        box(x, 137, cw, 37, tint, tint)
        text(x + 13, 146, title, 14, 'Bold', accent)
        text(x + cw - 13, 147, f'+{bonus}% / {1 + bonus / 100:.2f}x', 11.5, 'Bold', accent, 'right')
        for i, row in enumerate([r for r in ROWS if r[3] == bonus]):
            a, b, name, _, penalty, flair = row
            top = 184 + i * 70
            box(x, top, cw, 64)
            num = ROWS.index(row) + 1
            text(x + 11, top + 8, f'{num:02}', 9, 'Bold', accent)
            text(x + 34, top + 6, name, 13, 'Bold')
            pair(x + 12, top + 25, a, b, 7, 9)
            s = FRIENDLY.get(name, '+20% damage on the follow-up hit.')
            lines(x + 12, top + 42, s, cw - 24, 8.3, 9.4, MUTED, max_lines=2)
    text(40, 756, '+20% = 1.20x normal damage. +10% = 1.10x. +0% = 1.00x: the normal hit still deals damage.', 10, 'Bold', GROUPS[2][2])
    text(40, 776, 'Numbers are AI-guided balancing targets. Temporary effects depend on the actual target; live combat consistency is not yet verified.', 9, color=MUTED)
    C.showPage()


def group_page(g, page):
    bonus, title, accent, tint, subtitle = g
    header(f'REACTION GROUP {page - 1} / 3', title, subtitle, page)
    cw = (W - 98) / 2
    for i, row in enumerate([r for r in ROWS if r[3] == bonus]):
        a, b, name, _, penalty, flair = row
        x = 40 + (i % 2) * (cw + 18)
        top = 142 + (i // 2) * 150
        box(x, top, cw, 138)
        text(x + 15, top + 12, f'{ROWS.index(row) + 1:02}', 11, 'Bold', accent)
        text(x + 43, top + 8, name, 20, 'Bold')
        box(x + cw - 131, top + 10, 116, 25, tint, tint, 6)
        text(x + cw - 73, top + 16, f'+{bonus}% / {1 + bonus / 100:.2f}x', 12, 'Bold', accent, 'center')
        element(a, x + 42, top + 68, 18, True)
        text(x + 91, top + 62, '+', 17, color=MUTED, align='center')
        element(b, x + 140, top + 68, 18, True)
        arrow(x + 174, top + 68, x + 218, accent)
        effect = FRIENDLY.get(name, 'The compatible follow-up hit gains 20% extra damage.')
        lines(x + 235, top + 50, effect, cw - 253, 12, 16, font='Bold', max_lines=4)
        rule(x + 15, top + 107, x + cw - 15, top + 107)
        lines(x + 15, top + 115, flair, cw - 30, 10.4, 13, MUTED, max_lines=1)
    text(40, 756, 'One debuff per target. A new reaction debuff replaces the previous one; it never stacks indefinitely.', 10, 'Bold', accent)
    text(40, 776, 'Penalties end after the next applicable resolution or at the end of the following party turn. Anatomy, equipment and immunities still matter.', 9, color=MUTED)
    C.showPage()


def numbered_box(x, top, width, n, title, body, accent, tint):
    box(x, top, width, 140)
    fill(accent)
    C.circle(x + 28, H - top - 29, 14, fill=1, stroke=0)
    text(x + 28, top + 20, str(n), 15, 'Bold', '#ffffff', 'center')
    text(x + 52, top + 17, title, 18, 'Bold')
    lines(x + 18, top + 57, body, width - 36, 13, 18, max_lines=4)


def timing():
    header('TIMING + RESONANCE', 'Set it up. Follow through. Resonate.',
           'The setup and finisher can come from different characters. Enemies can use the same elemental combinations.', 5)
    bw = (W - 144) / 3
    numbered_box(40, 143, bw, 1, 'Land an elemental hit',
                 'A real eligible hit leaves one imprint on its exact target. Misses, full immunity and decorative effects leave none.', '#297ea6', '#e8f2f7')
    numbered_box(72 + bw, 143, bw, 2, 'Add a compatible hit',
                 'Use a separate action on that same target during this turn or the next. Either elemental order works.', '#7151a2', '#f1eafb')
    numbered_box(104 + 2 * bw, 143, bw, 3, 'Resolve the reaction',
                 'Consume the imprint, apply the listed payoff and earn +1 Resonance for the player who finishes it. Maximum one point per finisher per turn.', '#167a77', '#e3f4ef')
    arrow(40 + bw + 5, 211, 66 + bw, '#7151a2')
    arrow(72 + 2 * bw + 5, 211, 98 + 2 * bw, '#167a77')
    box(40, 302, W - 80, 75, '#eef3f5', '#eef3f5')
    text(58, 316, 'THE SHORT WINDOW', 10, 'Bold', '#297ea6')
    text(58, 339, 'Turn N: setup hit', 15, 'Bold')
    arrow(248, 348, 320, '#297ea6')
    text(340, 339, 'Same turn or N+1: compatible finisher', 15, 'Bold')
    arrow(755, 348, 819, '#297ea6')
    text(840, 339, 'Otherwise: imprint expires', 15, 'Bold')
    text(40, 401, '20 points unlock a ready surge', 24, 'Display')
    text(40, 438, '19 earned points + one completed reaction = 20 / 20. The filling reaction does not boost itself.', 13, color=MUTED)
    gx, gy, dotgap = 53, 484, 28
    for i in range(20):
        fill('#7151a2' if i < 19 else '#bc943d')
        C.circle(gx + i * dotgap, H - gy, 9, fill=1, stroke=0)
    text(625, 473, 'RESONANT', 18, 'Bold', '#7151a2')
    arrow(779, 484, 837, '#7151a2')
    text(856, 468, 'Next landed technique', 15, 'Bold')
    text(856, 491, '+50% ordinary damage', 13, 'Bold', '#7151a2')
    box(40, 531, (W - 98) / 2, 108)
    text(58, 546, 'Keeps the surge ready', 15, 'Bold', '#167a77')
    lines(58, 577, 'A miss, healing or utility action. Charge also carries between battles; rest and leveling do not earn it.', (W - 98) / 2 - 36, 13, 18, max_lines=3)
    x = 58 + (W - 98) / 2
    box(x, 531, (W - 98) / 2, 108)
    text(x + 18, 546, 'Spends the old charge', 15, 'Bold', '#7151a2')
    lines(x + 18, 577, 'A landed damaging spell or trained technique begun already ready. A reaction on that burst starts the next cycle at one.', (W - 98) / 2 - 36, 13, 18, max_lines=3)
    lines(40, 664, 'Remember: one imprint and one reaction debuff per target. At most one reaction per target per turn. A newer debuff replaces the old one. Physical slashing, piercing, bludgeoning and Soul do not prime or consume imprints.', W - 80, 12, 17, max_lines=3)
    text(40, 705, 'Damage example before mitigation: a 100-damage hit becomes 120 at +20%, 110 at +10%, or stays 100 at +0%.', 11, 'Bold', '#167a77')
    box(40, 733, W - 80, 48, '#fff0dc', '#fff0dc', 7)
    lines(54, 744, 'Implementation note: charge and learning transactions use native effects. Hit recognition, reaction percentages, brief combat penalties and expiry are AI-guided; these diagrams describe the current design, not verified live combat arithmetic.', W - 108, 10.5, 14, MUTED, max_lines=2)
    C.showPage()


def main():
    global C
    for p in [OUT, ARCHIVE, TMP]:
        p.mkdir(parents=True, exist_ok=True)
    dest = OUT / 'Elemental Reactions - Visual Reference.pdf'
    C = canvas.Canvas(str(dest), pagesize=(W, H), pageCompression=1)
    C.setTitle('Elemental Reactions - The Schools of Magic, Arise!')
    C.setAuthor('Voyage Maker')
    overview()
    for i, group in enumerate(GROUPS, 2):
        group_page(group, i)
    timing()
    C.save()
    pdf = PdfReader(dest)
    extracted = '\n'.join(p.extract_text() for p in pdf.pages)
    assert len(pdf.pages) == 5
    for a, b, name, *_ in ROWS:
        assert extracted.count(name) == 2, (name, extracted.count(name))
    assert all(e.title() in extracted for e in ELEMENTS)
    runtime = Path(sys.executable).resolve().parents[2]
    renderer = runtime / 'dependencies/native/poppler/Library/bin/pdftoppm.exe'
    if not renderer.exists():
        renderer = Path(shutil.which('pdftoppm') or '')
    assert renderer.is_file(), 'Poppler renderer is required for visual review.'
    # A3 at 220 dpi: approximately 3638 x 2573 px per reference sheet.
    subprocess.run([str(renderer), '-r', '220', '-png', str(dest), str(TMP / 'page')], check=True)
    names = ['01 - All Reactions', '02 - Impact Reactions', '03 - Damage and Disruption', '04 - Control Reactions', '05 - Timing and Resonance']
    pngs = []
    for i, name in enumerate(names, 1):
        target = OUT / (name + '.png')
        shutil.copyfile(TMP / f'page-{i}.png', target)
        pngs.append(target)
    # Small contact sheet is QA only, not a substitute for individual page review.
    thumbs = []
    for p in pngs:
        im = Image.open(p).convert('RGB')
        im.thumbnail((840, 594))
        thumbs.append(ImageOps.expand(im, border=8, fill='white'))
    sheet = Image.new('RGB', (1712, 1830), '#dce2e4')
    for i, im in enumerate(thumbs):
        sheet.paste(im, ((i % 2) * 856, (i // 2) * 610))
    sheet.save(TMP / 'contact-sheet.jpg', quality=93)
    note = OUT / 'Read Me.txt'
    note.write_text('Elemental Reactions - Visual Reference\n\nFive-page vector PDF plus five high-resolution PNG sheets.\n01: all 24 combinations\n02: impact\n03: damage and disruption\n04: control\n05: timing and Resonance\n\nBased on the current Magic Overhaul catalogue, 6 November 2026.\nNumerical effects are AI-guided design targets, not verified live combat math.\nNo gameplay JSON was edited for these diagrams.\n', encoding='utf-8')
    for p in [dest, *pngs, note]:
        shutil.copyfile(p, ARCHIVE / p.name)
    package = OUT.parent / 'Elemental Reactions - PDF and PNGs.zip'
    with zipfile.ZipFile(package, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in [dest, *pngs, note]:
            z.write(p, p.name)
    report = dict(pages=5, recipes=24, elements=16, visualReview='pending',
                  sourceSHA256=hashlib.sha256((HERE / 'reactions.json').read_bytes()).hexdigest(),
                  worldSHA256=hashlib.sha256((ROOT / 'world-draft/WorldAlpha - World.json').read_bytes()).hexdigest(),
                  outputs={p.name: dict(bytes=p.stat().st_size, sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in [dest, *pngs, package]},
                  liveCombatVerified=False)
    (HERE / 'diagram-review.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(pdf=str(dest), zip=str(package), contactSheet=str(TMP / 'contact-sheet.jpg'), pages=5)))


if __name__ == '__main__':
    main()
