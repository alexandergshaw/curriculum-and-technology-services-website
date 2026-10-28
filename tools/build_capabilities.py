"""Rebuild the public one-page curriculum services overview with ReportLab."""

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "access-capabilities.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
INK = colors.HexColor("#142e2b")
TEAL = colors.HexColor("#2d6452")
MUTED = colors.HexColor("#56635e")
SOFT = colors.HexColor("#e8ecdf")
LINE = colors.HexColor("#d3d9cd")
PAPER = colors.HexColor("#f5f3eb")
styles = {
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=14, textColor=MUTED),
    "small": ParagraphStyle("small", fontName="Helvetica", fontSize=8, leading=11, textColor=MUTED),
    "label": ParagraphStyle("label", fontName="Helvetica-Bold", fontSize=8, leading=11, textColor=TEAL),
    "heading": ParagraphStyle("heading", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=INK),
}
c = canvas.Canvas(str(OUTPUT), pagesize=(612, 792), pageCompression=1)
c.setTitle("Access Curriculum & Technology | Curriculum Services")
c.setAuthor("Alex Shaw and Baha Marupov | Access Curriculum & Technology")
c.setSubject("Course and program reviews, new computing courses, and the Annual Curriculum Partnership")
c.setFillColor(PAPER)
c.rect(0, 0, 612, 792, fill=1, stroke=0)
c.setFillColor(TEAL)
c.rect(0, 784, 612, 8, fill=1, stroke=0)


def paragraph(text, x, y, width, style="body"):
    item = Paragraph(text, styles[style])
    _, height = item.wrap(width, 750)
    assert y - height >= 35, f"Text exceeds the page: {text[:50]}"
    item.drawOn(c, x, y - height)
    return y - height


def rule(y):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.7)
    c.line(42, y, 570, y)


c.setFillColor(INK)
c.setFont("Helvetica-Bold", 27)
c.drawString(42, 741, "Access.")
paragraph("CURRICULUM &amp; TECHNOLOGY", 43, 729, 300, "label")
c.setFillColor(MUTED)
c.setFont("Helvetica", 8)
c.drawRightString(570, 750, "ALEX SHAW + BAHA MARUPOV")
c.drawRightString(570, 735, "Omaha, Nebraska | Serving the Midwest")
rule(707)
c.setFillColor(INK)
c.setFont("Helvetica", 29)
c.drawString(42, 670, "Modernize or create")
c.setFillColor(TEAL)
c.setFont("Times-Italic", 32)
c.drawString(42, 634, "computing courses.")
y = paragraph(
    "Alex Shaw and Baha Marupov are software professionals and college educators. "
    "We help colleges update computing courses and programs, and create new courses.",
    42, 614, 528,
)

y = paragraph(
    "While teaching at colleges, we saw how quickly technology changes - and how much "
    "work it takes to keep courses current while teaching and supporting students. "
    "Access exists to help with that work.", 42, y - 12, 528,
)
y = paragraph(
    "College budgets can also make it difficult to match the salaries offered by technology companies.",
    42, y - 7, 528, "small",
)

top = y - 18
paragraph("THREE WAYS WE CAN HELP", 42, top, 528, "label")
top -= 22
services = [
    (
        "Review and update<br/>courses and programs",
        "A defined project reviews content, tools, learning goals, prerequisites, and "
        "course sequence. Receive a prioritized plan and agreed revisions to materials "
        "and assessments.",
    ),
    (
        "Create a new<br/>computing course",
        "Develop a course plan with lessons, labs, projects, assessments, and instructor "
        "guidance. Receive editable materials that your faculty can use and adapt.",
    ),
]
bottoms = []
for i, (title, body) in enumerate(services):
    x = 42 + i * 276
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.7)
    c.line(x, top, x + 252, top)
    bottom = paragraph(title, x, top - 11, 252, "heading")
    bottoms.append(paragraph(body, x, bottom - 8, 252))

box_top = min(bottoms) - 18
box_bottom = box_top - 157
c.setFillColor(SOFT)
c.rect(42, box_bottom, 528, 157, fill=1, stroke=0)
y = paragraph("ANNUAL CURRICULUM PARTNERSHIP", 57, box_top - 14, 498, "label")
y = paragraph("Keep courses and programs current", 57, y - 7, 498, "heading")
y = paragraph(
    "An annual review, agreed updates, and faculty consultation during the year help "
    "your courses and programs reflect changes in technology and workforce needs.",
    57, y - 8, 498,
)
y = paragraph("Review together / agree priorities / update materials / review the changes with faculty", 57, y - 12, 498)
y = paragraph(
    "Receive updated materials, a record of changes, remaining priorities, and a plan "
    "for the next year.", 57, y - 8, 498,
)
assert y >= box_bottom + 12, "Annual partnership text overflows its panel"

y = paragraph("AGREE ON THE WORK BEFORE WE BEGIN", 42, box_bottom - 15, 528, "label")
y = paragraph(
    "We agree on the covered courses or program, revisions, consultation, schedule, "
    "and fee. Additional work is scoped separately. Faculty make the academic "
    "decisions and approve the finished work.", 42, y - 7, 528,
)
assert y >= 104, "Scope agreement overlaps the contact footer"
rule(89)
paragraph("CONTACT ALEX ABOUT YOUR COURSES OR PROGRAM", 42, 76, 310, "label")
paragraph('<link href="mailto:alexandergshaw@gmail.com" color="#2d6452">alexandergshaw@gmail.com</link>', 42, 59, 310)
paragraph(
    '<link href="mailto:alexandergshaw@gmail.com?subject=Annual%20Curriculum%20Partnership" '
    'color="#2d6452">Ask about the Annual<br/>Curriculum Partnership</link>',
    390, 73, 180, "small",
)
c.showPage()
c.save()
print(OUTPUT)
