#!/usr/bin/python3
################################################################################
from reportlab.pdfgen import canvas
################################################################################
c = canvas.Canvas("pdf-example1.pdf")
c.drawString(100,750,"Just created a simple PDF with Python!")
c.save()
################################################################################
canvas = canvas.Canvas("pdf-example2.pdf")
canvas.setLineWidth(.4)
canvas.setFont('Helvetica', 14)
canvas.drawString(40,750,'DATE')
from datetime import date
canvas.drawString(400,750,str(date.today()))
canvas.line(380,747,540,747)
canvas.drawString(40,725,'NAME:')
name = input("What is your name? ")
canvas.drawString(400,725,name)
canvas.line(380,723,540,723)
canvas.save()
################################################################################
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.units import cm
################################################################################
doc = SimpleDocTemplate("pdf-example3.pdf",pagesize=letter,
                        rightMargin=60,leftMargin=60,
                        topMargin=40,bottomMargin=40)
CustomReport=[]
# Add image
fig = "python-scripting.png"
im = Image(fig, 400, 400)
# im = Image(fig, 4*cm, 4*cm)
CustomReport.append(im)
# Add text
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
ptext = 'This is the first line of text which should be long enough to check if the justify works.\
    Let me add some dummy text like: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed\
    do eiusmod tempor incididunt ut labore et dolore magna aliqua'
CustomReport.append(Paragraph(ptext, styles["Justify"]))
CustomReport.append(Spacer(1, 12))
# Finally add a table
data=  [['c0r0', 'c1r0', 'c2r0', 'c3r0', 'c4r0'],
        ['c0r1', 'c1r1', 'c2r1', 'c3r1', 'c4r1'],
        ['c0r2', 'c1r2', 'c2r2', 'c3r2', 'c4r2'],
        ['c0r3', 'c1r3', 'c2r3', 'c3r3', 'c4r3']]
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
t=Table(data,style=[('GRID',(0,0),(1,1),2,colors.green),
                    ('BOX',(2,2),(-1,-1),1,colors.red),
                    ('BOX',(0,3),(1,3),1,colors.orange),
                    ('LINEABOVE',(2,3),(3,3),2,colors.blue),
                    ])
t.setStyle(TableStyle([('TEXTCOLOR',(1,1),(-2,-2),colors.red),
    ('LINEBEFORE',(3,0),(3,0),2,colors.black),
    ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
    ]))
CustomReport.append(t)
# Write pdf document
doc.build(CustomReport)
################################################################################