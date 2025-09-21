from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from .report_text import build_report

def export_pdf(filepath, corr, scenario, es_cum, charts=[]):
    doc = SimpleDocTemplate(filepath, pagesize=A4)
    styles = getSampleStyleSheet()
    flow = []
    txt = build_report(corr, scenario, es_cum)
    for line in txt.split("\n"):
        flow.append(Paragraph(line, styles["Normal"]))
        flow.append(Spacer(1, 6))
    for chart in charts:
        flow.append(Image(chart, width=400, height=250))
        flow.append(Spacer(1, 12))
    doc.build(flow)
