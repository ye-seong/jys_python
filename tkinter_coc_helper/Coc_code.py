import tkinter as tk
from tkinter import * 
import re


class Coc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Coc Helper')
        self.geometry('400x500')
        self.resizable(False, False)

        self.barF = tk.Frame(self)
        self.desc_rowF1 = tk.Frame(self)
        self.desc_rowF2 = tk.Frame(self)
        self.bup_rowF1 = tk.Frame(self)

        self.descBtn = Button(self.barF, text='/desc삽입', command=self.DescMode)
        self.backupBtn = Button(self.barF, text='백업헬퍼', command=self.BackupMode)

        self.text = Text(self.desc_rowF1, height=10, width=55)
        self.turnBtn = Button(self.desc_rowF1, text='실행', command=self.Turn)
        self.turnBtn1 = Button(self.desc_rowF1, text='또먼기능하지', command=self.Turn)
        self.result = Text(self.desc_rowF2, height=10, width=55)

        self.buptext = Text(self.bup_rowF1, height=10, width=55)
        self.sizeLabel = Label(self.bup_rowF1, text='박스 사이즈를 px을 포함하여 작성해주세요.')
        self.sizeEntry = Entry(self.bup_rowF1)

    def initWindow(self):
        self.barF.pack()
        self.desc_rowF1.pack()
        self.desc_rowF2.pack()
        self.descBtn.pack(side=LEFT)
        self.backupBtn.pack(side=LEFT)
        self.text.pack(pady=10)
        self.buptext.pack()
        self.sizeLabel.pack()
        self.sizeEntry.pack()
        self.turnBtn.pack(side=LEFT, ipadx=30, ipady=1, padx=50, pady=10)
        self.turnBtn1.pack(side=RIGHT, ipadx=30, ipady=1, padx=50, pady=10)
        self.result.pack()

    def DescMode(self):
        self.desc_rowF1.pack()
        self.desc_rowF2.pack()
        self.bup_rowF1.forget()

    def BackupMode(self):
        self.desc_rowF1.forget()
        self.desc_rowF2.forget()
        self.bup_rowF1.pack()

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


if __name__=="__main__":
    coc = Coc()
    coc.initWindow()
    coc.mainloop()