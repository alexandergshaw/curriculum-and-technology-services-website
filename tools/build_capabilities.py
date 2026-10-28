"""Rebuild the public, one-page capabilities brief with ReportLab."""

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "access-capabilities.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

INK = colors.HexColor("#142d3c")
TEAL = colors.HexColor("#245c59")
MUTED = colors.HexColor("#52616a")
SOFT = colors.HexColor("#edf1eb")
LINE = colors.HexColor("#d7dcd6")
PAPER = colors.HexColor("#fcfbf7")

styles = {
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10, leading=14, textColor=MUTED),
    "small": ParagraphStyle("small", fontName="Helvetica", fontSize=8, leading=11, textColor=MUTED),
    "label": ParagraphStyle("label", fontName="Helvetica-Bold", fontSize=8, leading=11, textColor=TEAL),
    "heading": ParagraphStyle("heading", fontName="Times-Roman", fontSize=17, leading=20, textColor=INK),
    "service": ParagraphStyle("service", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=INK),
}

c = canvas.Canvas(str(OUTPUT), pagesize=(612, 792), pageCompression=1)
c.setTitle("Access Curriculum & Technology | Capabilities")
c.setAuthor("Access Curriculum & Technology")
c.setSubject("Services, professional experience, and an example focused course review")
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
c.setFont("Times-Roman", 30)
c.drawString(42, 740, "Access.")
paragraph("CURRICULUM &amp; TECHNOLOGY", 43, 727, 300, "label")
c.setFillColor(MUTED)
c.setFont("Helvetica", 8)
c.drawRightString(570, 750, "CAPABILITIES / OCTOBER 2026")
c.drawRightString(570, 735, "Omaha, Nebraska | Serving the Midwest")
rule(706)

c.setFillColor(INK)
c.setFont("Times-Roman", 28)
c.drawString(42, 671, "Practical computing curriculum.")
c.setFillColor(TEAL)
c.setFont("Times-Italic", 28)
c.drawString(42, 639, "Built with your faculty.")
y = paragraph(
    "We help Midwest colleges align computing courses with program goals, develop applied "
    "assessments, and equip faculty with editable teaching materials and a practical implementation plan.",
    42, 619, 528,
)

top = y - 23
paragraph("THREE WAYS TO BEGIN", 42, top, 528, "label")
top -= 22
services = [
    ("Update a course", "Outcomes and module plans. Applied labs, projects, and rubrics. Editable instructor materials and implementation guidance."),
    ("Build a new offering", "Competency frameworks and prerequisites. Course sequences and assessment plans. Course development and phased implementation."),
    ("Plan improvements", "Curriculum and assessment maps. Prioritized findings. A modernization roadmap with implementation considerations."),
]
bottoms = []
for i, (title, body) in enumerate(services):
    x = 42 + i * 182
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.7)
    c.line(x, top, x + 164, top)
    bottom = paragraph(title, x, top - 10, 164, "service")
    bottoms.append(paragraph(body, x, bottom - 8, 164))

y = min(bottoms) - 14
y = paragraph("Faculty workshops, LMS packaging, technical setup, and ongoing updates can support these engagements.", 42, y, 528, "small")

box_top = y - 18
box_bottom = box_top - 194
c.setFillColor(SOFT)
c.rect(42, box_bottom, 528, 194, fill=1, stroke=0)
y = paragraph("EXAMPLE ENGAGEMENT", 57, box_top - 13, 498, "label")
y = paragraph("Focused course review", 57, y - 5, 498, "heading")
for text in [
    "<b>Review:</b> Syllabus, course and program outcomes, selected assignments and rubrics, and faculty priorities.",
    "<b>Receive:</b> An editable outcomes-to-assessment map, prioritized findings, and a recommended sequence of updates.",
    "<b>Collaborate:</b> Kickoff, feedback on draft findings, and handoff. Faculty retain academic decisions and approval.",
    "<b>Plan:</b> A written proposal sets the schedule, fee, review windows, and deliverables after an initial scope discussion.",
]:
    y = paragraph(text, 57, y - 6, 498)
assert y >= box_bottom + 8, "Engagement text overflows its panel"

y = box_bottom - 18
y = paragraph("LED BY ALEX SHAW", 42, y, 528, "label")
y = paragraph(
    "Software-engineering leadership, including lead engineering work at Mutual of Omaha, "
    "alongside teaching and curriculum-development experience at Metropolitan Community College "
    "and Midland University. Based in Omaha and available to colleges across the Midwest.",
    42, y - 6, 528,
)
y = paragraph("Affiliations describe Alex's individual experience, not consulting client relationships or institutional endorsements.", 42, y - 6, 528, "small")
assert y >= 91, "Biography overlaps the contact footer"

rule(82)
paragraph("LET'S DISCUSS YOUR PROGRAM", 42, 70, 280, "label")
paragraph('<link href="mailto:alexandergshaw@gmail.com" color="#245c59">alexandergshaw@gmail.com</link>', 42, 55, 290)
paragraph("Share the course or program, the challenge,<br/>and any timing constraints.", 360, 67, 210, "small")
c.showPage()
c.save()
print(OUTPUT)
