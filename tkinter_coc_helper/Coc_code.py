import tkinter as tk
from tkinter import * 
import re
from tkinter.font import *



class Coc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Coc Helper')
        self.geometry('400x500')
        self.resizable(False, False)

        self.boxsizeval = tk.BooleanVar()
        self.decoval = tk.BooleanVar()

        self.barF = tk.Frame(self)
        self.desc_rowF1 = tk.Frame(self)
        self.desc_rowF2 = tk.Frame(self)
        self.bup_rowF1 = tk.Frame(self)
        self.bup_rowF2 = tk.Frame(self)

        self.descBtn = Button(self.barF, text='/desc삽입',  width=20, command=self.DescMode)
        self.backupBtn = Button(self.barF, text='백업헬퍼', width=20, command=self.BackupMode)

        self.text = Text(self.desc_rowF1, height=10, width=55)
        self.turnBtn = Button(self.desc_rowF1, text='실행', bg='yellow', command=self.Turn)
        self.result = Text(self.desc_rowF2, height=10, width=55)

        self.buptext = Text(self.bup_rowF1, height=10, width=55)
        self.sizeLabel = Label(self.bup_rowF1, text='박스 사이즈 (px포함) : ')
        self.sizeEntry = Entry(self.bup_rowF1)
        self.boxsizeCheck = Checkbutton(self.bup_rowF2, variable=self.boxsizeval, text='박스사이즈 100%로 변경')
        self.decoCheck = Checkbutton(self.bup_rowF2, variable=self.decoval, text='밑줄제거')
        self.bupBtn = Button(self.bup_rowF2, text='실행', command=self.BackUp)

    def initWindow(self):
        self.barF.pack(pady=10)
        self.desc_rowF1.pack()
        self.desc_rowF2.pack()
        self.descBtn.pack(side=LEFT, padx=5)
        self.backupBtn.pack(side=LEFT)
        self.text.pack()
        self.buptext.pack()
        self.sizeLabel.pack(side=LEFT, padx=10, pady=10)
        self.sizeEntry.pack(side=LEFT, pady=10)
        self.boxsizeCheck.pack()
        self.decoCheck.pack()
        self.bupBtn.pack(side=BOTTOM, ipadx=50, ipady=30, pady=100)
        self.turnBtn.pack(side=RIGHT, ipadx=50, ipady=1, padx=10, pady=10)
        self.result.pack()

    def DescMode(self):
        self.desc_rowF1.pack()
        self.desc_rowF2.pack()
        self.bup_rowF1.forget()
        self.bup_rowF2.forget()

    def BackupMode(self):
        self.desc_rowF1.forget()
        self.desc_rowF2.forget()
        self.bup_rowF1.pack()
        self.bup_rowF2.pack()

    def Turn(self):
        text = self.text.get('1.0', 'end-1c')
        arr = re.findall(r'[^.!?\n]+[.!?]+|[^\n]+', text)
        result = ''
        for i in arr:
            if i[0] == ' ':
                result = result + '/desc' + i + '\n'
            else:
                result = result + '/desc ' + i + '\n'
        self.Return(result)

    def Return(self, text):
        self.result.delete(1.0, END)
        self.result.insert(END, text)

    def BackUp(self):
        text = self.buptext.get('1.0', 'end-1c')
        px = self.sizeEntry.get()
        result = text
        if self.boxsizeval.get() :
            if px == '':
                pass
            else:
                result = result.replace(px, '100%')
        if self.decoval.get() :
            result = result.replace('style="', 'style="text-decoration: none; ')

        self.buptext.delete(1.0, END)
        self.buptext.insert(END, result)

        
if __name__=="__main__":
    coc = Coc()
    coc.initWindow()
    coc.mainloop()