import tkinter as tk
from tkinter import * 
import re


class Coc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Coc Helper')
        self.geometry('400x500')
        self.resizable(False, False)

        self.rowF1 = tk.Frame(self)
        self.rowF2 = tk.Frame(self)

        self.text = Text(self.rowF1, height=10, width=55)
        self.turnBtn = Button(self.rowF1, text='실행', command=self.Turn)
        self.turnBtn1 = Button(self.rowF1, text='실행1', command=self.Turn)
        self.result = Text(self.rowF2, height=10, width=55)

    def initWindow(self):
        self.rowF1.pack()
        self.rowF2.pack()
        self.text.pack(pady=10)
        self.turnBtn.pack(side=LEFT, padx=5, pady=10)
        self.turnBtn1.pack(side=LEFT, padx=5, pady=10)
        self.result.pack()

    def Turn(self):
        text = self.text.get('1.0', 'end-1c')
        arr = re.findall(r'.*?\.+|\S.*?(?=\n|$)', text)
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