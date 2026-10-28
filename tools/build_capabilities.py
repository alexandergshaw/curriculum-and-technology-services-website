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
c.setTitle("Alex Shaw | Computing Course Development")
c.setAuthor("Alex Shaw | Access Curriculum & Technology")
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
c.drawRightString(570, 750, "ALEX SHAW / COURSE DEVELOPMENT")
c.drawRightString(570, 735, "Omaha, Nebraska | Serving the Midwest")
rule(707)
c.setFillColor(INK)
c.setFont("Helvetica", 29)
c.drawString(42, 670, "Modernize or create")
c.setFillColor(TEAL)
c.setFont("Times-Italic", 32)
c.drawString(42, 634, "computing courses.")
y = paragraph(
    "I'm a software professional and a teaching professional. I bring both kinds of "
    "experience to developing courses for your college - with practical projects, "
    "clear assessments, and materials ready to teach.", 42, 614, 528,
)

top = y - 23
paragraph("TWO WAYS I CAN HELP", 42, top, 528, "label")
top -= 22
services = [
    ("Modernize an existing course", "Review the syllabus and existing materials. Update technologies, examples, and applied projects. Refine assessments, rubrics, and instructor guidance."),
    ("Create a new computing course", "Define outcomes, prerequisites, and a module plan. Build lessons, labs, projects, and assessments. Prepare editable teaching materials and a faculty handoff."),
]
bottoms = []
for i, (title, body) in enumerate(services):
    x = 42 + i * 276
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.7)
    c.line(x, top, x + 252, top)
    bottom = paragraph(title, x, top - 11, 252, "heading")
    bottoms.append(paragraph(body, x, bottom - 9, 252))

y = min(bottoms) - 25
paragraph("SOFTWARE EXPERIENCE + TEACHING EXPERIENCE", 42, y, 528, "label")
y = paragraph(
    "<b>Software professional.</b> My background includes enterprise software-engineering "
    "leadership and lead engineering work at Mutual of Omaha.", 42, y - 20, 528,
)
y = paragraph(
    "<b>Teaching professional.</b> My teaching and curriculum-development experience "
    "includes Metropolitan Community College and Midland University, with work in web "
    "development instruction and systems administration curriculum design.", 42, y - 10, 528,
)
y = paragraph(
    "Affiliations describe my individual experience, not consulting client relationships or institutional endorsements.",
    42, y - 9, 528, "small",
)

box_top = y - 19
box_bottom = box_top - 105
c.setFillColor(SOFT)
c.rect(42, box_bottom, 528, 105, fill=1, stroke=0)
y = paragraph("WORKING WITH YOUR FACULTY", 57, box_top - 14, 498, "label")
y = paragraph(
    "We agree on the learners, course goals, deliverables, timeline, and fee. I develop "
    "the materials with faculty feedback and provide a clear handoff. Faculty retain "
    "academic decisions and approval.", 57, y - 9, 498,
)
assert y >= box_bottom + 12, "Working-together text overflows its panel"
assert box_bottom >= 111, "Content overlaps the contact footer"
rule(89)
paragraph("LET'S TALK ABOUT YOUR COURSE", 42, 76, 310, "label")
paragraph('<link href="mailto:alexandergshaw@gmail.com" color="#2d6452">alexandergshaw@gmail.com</link>', 42, 59, 310)
paragraph("Tell me what you teach, what needs to change,<br/>or what new course you want to offer.", 360, 75, 210, "small")
c.showPage()
c.save()
print(OUTPUT)
