import tkinter as tk
from tkinter import filedialog as fd

import readCSV
from printPDF import PDF


class tagGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("700x700")
        self.root.title("Chapel Hill Wine Company Tagging System")

        self.wineLabel = tk.Label(self.root, text="Wine Name", font=('Arial', 18), fg='white')
        self.wineLabel.pack(padx=10, pady=10)
        self.wineName = tk.Entry(self.root)
        self.wineName.pack()

        self.sizeLabel = tk.Label(self.root, text="Case Size", font=('Arial', 18), fg='white')
        self.sizeLabel.pack(padx=10, pady=10)
        self.caseSize = tk.Entry(self.root)
        self.caseSize.pack()
        self.path = '/Users/thomascox/Documents/CHW_Project/Tom tagging list.csv'
        self.pdf = None
        self.lineCount = 0
        self.output = '/Users/thomascox/Documents/CHW_Project/Output/tags.pdf'

        self.button = tk.Button(self.root, text="Select File", font=('Arial', 16), command=self.selectFile)
        self.button.pack()

        self.button = tk.Button(self.root, text="Create Tags", font=('Arial', 16), command=self.tagWine)
        self.button.pack()

        self.button = tk.Button(self.root, text="Print Tags", font=('Arial', 16), command=self.printTags)
        self.button.pack()

        #self.button = tk.Button(self.root, text="New Wine", font=('Arial', 16), command=self.printTags())
        #self.button.pack()

        self.root.mainloop()

    def selectFile(self):
        self.path = fd.askopenfilename(title='Select a File', initialdir='/Users/thomascox/Documents/CHW_Project',
                                       filetypes=[("CSV files", "*.csv")])

    def tagWine(self):
        name = self.wineName.get()
        size = int(self.caseSize.get())
        path = self.path
        tags = readCSV.read(path, name, size)
        if self.pdf is None:
            self.pdf = PDF.__new__(PDF)
        self.pdf.printPDF(tags)
        print(self.pdf.lineCount)

        # self.pdf, self.lineCount = readCSV.printPDF(tags, self.pdf, self.lineCount)

    def printTags(self):
        print(self.wineName.get())
        if self.pdf is not None:
            self.pdf.out()

tagGUI()
