from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap

def export_segments_to_pdf(segments, out_path):
    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4

    y = height - 40
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "Transcrição de Áudio")
    y -= 40
    c.setFont("Helvetica", 10)

    for seg in segments:
        if isinstance(seg, dict):
            text = f"[{seg.get('start', ''):.2f}s - {seg.get('end', ''):.2f}s] {seg.get('speaker', '')}: {seg.get('text', '')}"
        else:
            text = str(seg)
        for line in textwrap.wrap(text, width=110):
            if y < 70:
                c.showPage()
                y = height - 40
                c.setFont("Helvetica", 10)
            c.drawString(40, y, line)
            y -= 16
        y -= 4  # Espaço extra entre segmentos

    c.save()
    return out_path
