from fpdf import FPDF
import pandas as pd

pdf=FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(False,margin=0)
df=pd.read_csv("topics.csv",sep=",")
for index,row in df.iterrows():
    pdf.add_page()
    for y in range(20,298,10):
        pdf.line(10,y,200,y)

    #Set the header
    pdf.set_font("Times",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12,txt=f"{row['Topic']}",
             align="L",ln=1,border=1)

    # Set footer
    pdf.ln(265)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=10,txt= row['Topic'],align="R")

    for i in range(row['Pages']-1):
        #Set the footer
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
