"""Rebuild the public one-page course-development overview with ReportLab."""

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
c.setTitle("Access Curriculum & Technology | Computing Course Development")
c.setAuthor("Alex Shaw and Baha Marupov | Access Curriculum & Technology")
c.setSubject("Software and teaching expertise to modernize or create computing courses")
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
    "We help faculty update computing courses or create new ones - with practical "
    "projects, clear assessments, and materials ready to teach.", 42, 614, 528,
)

top = y - 20
paragraph("WHY ACCESS EXISTS", 42, top, 528, "label")
y = paragraph(
    "While teaching at colleges, Alex and Baha saw a recurring challenge: technology "
    "changes quickly, but keeping courses current takes time that faculty must balance "
    "with teaching and supporting students. Access exists to help with that work.",
    42, top - 19, 528,
)
y = paragraph(
    "College budgets can also make it difficult to match the salaries offered by technology companies.",
    42, y - 7, 528, "small",
)

top = y - 20
paragraph("TWO WAYS WE CAN HELP", 42, top, 528, "label")
top -= 22
services = [
    ("Modernize an existing course", "Review the syllabus and existing materials. Update technologies, examples, and applied projects. Refine assessments, rubrics, and instructor guidance."),
    ("Create a new computing course", "Set learning goals, prerequisites, and a course plan. Build lessons, labs, projects, and assessments. Prepare editable teaching materials and guidance for faculty."),
]
bottoms = []
for i, (title, body) in enumerate(services):
    x = 42 + i * 276
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.7)
    c.line(x, top, x + 252, top)
    bottom = paragraph(title, x, top - 11, 252, "heading")
    bottoms.append(paragraph(body, x, bottom - 9, 252))

y = min(bottoms) - 21
paragraph("SOFTWARE EXPERIENCE + TEACHING EXPERIENCE", 42, y, 528, "label")
top = y - 20
bottoms = []
for i, name in enumerate(("Alex Shaw", "Baha Marupov")):
    x = 42 + i * 276
    bottom = paragraph(name, x, top, 252, "heading")
    bottoms.append(paragraph("Software professional<br/>College educator", x, bottom - 5, 252))
y = min(bottoms)

box_top = y - 18
box_bottom = box_top - 89
c.setFillColor(SOFT)
c.rect(42, box_bottom, 528, 89, fill=1, stroke=0)
y = paragraph("WORKING WITH YOUR FACULTY", 57, box_top - 14, 498, "label")
y = paragraph(
    "We agree on the course goals, materials, schedule, and fee. We develop the "
    "materials with faculty feedback and explain how to use and update them. "
    "Your faculty make the academic decisions and approve the finished work.", 57, y - 9, 498,
)
assert y >= box_bottom + 12, "Working-together text overflows its panel"
assert box_bottom >= 111, "Content overlaps the contact footer"
rule(89)
paragraph("CONTACT ALEX ABOUT YOUR COURSE", 42, 76, 310, "label")
paragraph('<link href="mailto:alexandergshaw@gmail.com" color="#2d6452">alexandergshaw@gmail.com</link>', 42, 59, 310)
paragraph("Tell us what you teach, what needs to change,<br/>or what new course you want to offer.", 360, 75, 210, "small")
c.showPage()
c.save()
print(OUTPUT)
