import time
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate

formatted_time = time.ctime()
doc = SimpleDocTemplate("test_report_lab.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
doc.pagesize = landscape(A4)
canvas = canvas.Canvas("f.pdf", pagesize=letter)
canvas.setLineWidth(.3)
#s = Spacer(1, 0.25)


canvas.setFont('Helvetica', 20)
canvas.drawString(260, 750, 'RELATÓRIO',None, 1)
canvas.line(260, 747, 383, 747)

canvas.setFont('Helvetica', 12)
canvas.drawString(445, 730, formatted_time)
canvas.line(25, 725, 585, 725)

canvas.line(25, 725, 25, 705)
canvas.drawString(30, 710, 'COD')
canvas.line(85, 725, 85, 705)
canvas.drawString(145, 710, 'NOME')
canvas.line(250, 725, 250, 705)
canvas.drawString(275, 710, 'RG')
canvas.line(320, 725, 320, 705)
canvas.drawString(365, 710, 'CPF')
canvas.line(400, 725, 400, 705)
canvas.line(585, 725, 585, 705)
canvas.line(25, 705, 585, 705)

canvas.save()