from fpdf import FPDF

class PDF:
    pdf = None
    lineCount=0
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self):
        self.pdf = None
        self.lineCount = 0


    def printPDF(self, tags):
        if self.pdf is None:
            self.pdf = FPDF()
            self.pdf.add_page()
        while len(tags) > 0:
            print("Test")
            if self.lineCount > 5:
                self.pdf.add_page()
                self.lineCount = 0
            tagL = tags[len(tags) - 1]
            tags.pop()
            if len(tags) > 0:
                tagR = tags[len(tags) - 1]
                tags.pop()
                addRight(self.pdf, tagL, tagR)
                self.lineCount += 1
            else:
                addLeft(self.pdf, tagL)
                self.lineCount += 1

        # align_index = (align_index+1)%2
        # line = (line+1)%2
    def out(self):
        self.pdf.output("/Users/thomascox/Documents/CHW_Project/Tags.pdf")
        self.pdf.close()

def addLeft(pdf, tag):
    align = ['L', 'R']
    align_index = 0
    line = 1
    w = 5
    h = 10
    last_font = 17
    first_font = 12
    wine_font = 14
    pdf.set_font("Arial", 'B', size=last_font)
    txt = tag['last']
    pdf.cell(w, h, txt=txt, ln=line, align=align[align_index])
    pdf.set_font("Arial", size=first_font)
    txt = tag['first']
    pdf.cell(w, h, txt=txt, ln=line, align=align[align_index])
    pdf.set_font("Arial", size=wine_font)
    txt = tag['qty']
    pdf.cell(w, h, txt=txt, ln=0, align=0)
    txt = '-'
    pdf.cell(w, h, txt=txt, ln=0, align=0)
    txt = tag['wine']
    pdf.cell(w, h, txt=txt, ln=1, align=0)
    txt = '\n'
    pdf.cell(w, h, txt=txt, ln=1, align=0)


def addRight(pdf, tagL, tagR):
    align = ['L', 'R']
    L = 0
    R = 1
    line = 0
    w = 5
    h = 10
    last_font = 17
    first_font = 12
    wine_font = 14
    pdf.set_font("Arial", 'B', size=last_font)
    txt = tagL['last']
    pdf.cell(75, h, txt=txt, ln=0, align=align[L])
    txt = tagR['last']
    pdf.cell(75, h, txt=txt, ln=1, align=align[L])
    pdf.set_font("Arial", size=first_font)
    txt = tagL['first']
    pdf.cell(75, h, txt=txt, ln=0, align=align[L])
    txt = tagR['first']
    pdf.cell(75, h, txt=txt, ln=1, align=align[L])
    pdf.set_font("Arial", size=wine_font)
    txt = tagL['qty']
    pdf.cell(w, h, txt=txt, ln=0, align=align[L])
    txt = '-'
    pdf.cell(w, h, txt=txt, ln=0, align=align[L])
    txt = tagL['wine']
    pdf.cell(65, h, txt=txt, ln=0, align=align[L])
    txt = tagR['qty']
    pdf.cell(w, h, txt=txt, ln=0, align=align[L])
    txt = '-'
    pdf.cell(w, h, txt=txt, ln=0, align=align[L])
    txt = tagR['wine']
    pdf.cell(w, h, txt=txt, ln=1, align=align[L])
    txt = '\n'
    pdf.cell(w, h, txt=txt, ln=1, align=0)

