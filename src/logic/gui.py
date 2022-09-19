# Initializing window
from re import X
import tkinter as tk
import tkinter.font as tkFont
from tkinter import scrolledtext
import time

from capture import Capture


class GUI:
    def __init__(self, root):
        #setting title
        root.title("GT")
        #setting window size
        width=500
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        root.config(bg='#4a7a8c')
        root.wm_attributes('-transparentcolor','#4a7a8c')



        
        contentsFrame=tk.Frame(root)
        contentsFrame.place(x=0, y=50,width=500, height=250)
        GLabel_157=tk.Label(contentsFrame)
        GLabel_157["activebackground"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_157["font"] = ft
        GLabel_157["fg"] = "#333333"
        GLabel_157["justify"] = "center"
        GLabel_157["text"] = "현재가"
        GLabel_157.place(x=10,y=10,width=69,height=31)

        # def value_check(self):
        #     GLabel_157.config(text="숫자를 입력하세요.")
        #     valid = False
        #     if self.isdigit():
        #         if (int(self) <= 50 and int(self) >= 0):
        #             valid = True
        #         elif self == '':
        #             valid = True
        #     return valid

        # def value_error(self):
        #     GLabel_157.config(text=str(self) + "를 입력하셨습니다.\n올바른 값을 입력하세요.")

        # validate_command=(root.register(value_check), '%P')
        # invalid_command=(root.register(value_error), '%P')
        GLineEdit_462=tk.Spinbox(contentsFrame)
        # GLineEdit_462["validate"] = "all"
        # GLineEdit_462["validatecommand"] = validate_command
        # GLineEdit_462["invalidcommand"] = invalid_command
        GLineEdit_462["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_462["font"] = ft
        GLineEdit_462["fg"] = "#333333"
        GLineEdit_462["justify"] = "right"
        GLineEdit_462["text"] = ""
        GLineEdit_462.place(x=80,y=10,width=292,height=30)

        GButton_237=tk.Button(contentsFrame)
        GButton_237["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_237["font"] = ft
        GButton_237["fg"] = "#000000"
        GButton_237["justify"] = "center"
        GButton_237["text"] = "재생"
        GButton_237.place(x=380,y=10,width=44,height=30)
        GButton_237["command"] = self.GButton_237_command


        GButton_390=tk.Button(contentsFrame)
        GButton_390["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_390["font"] = ft
        GButton_390["fg"] = "#000000"
        GButton_390["justify"] = "center"
        GButton_390["text"] = "중지"
        GButton_390.place(x=430,y=10,width=44,height=30)
        GButton_390["command"] = self.GButton_390_command

        self.st = scrolledtext.ScrolledText(contentsFrame, wrap=tk.WORD, font=tkFont.Font(family='Times',size=10))        
        self.st.place(x=30,y=50,width=420,height=190)
        self.log('init')


    def GButton_237_command(self):
        self.log('play')
        x = root.winfo_x()
        y = root.winfo_y()
        
        xBias = 10
        yBias = 30
        c = Capture(x + xBias, y + yBias, x + 500 - xBias, y + 50 + yBias)
        str = c.imageToString()

        self.log(''.join(["인식된 숫자: ", str]))
        
    def GButton_390_command(self):
        self.log('stop')

    def log(self, text = "-"):
        tm = time.localtime()
        self.st.configure(state ='normal')
        self.st.insert(tk.INSERT, f'[{tm.tm_year}-{tm.tm_mon}-{tm.tm_mday} {tm.tm_hour}:{tm.tm_min}:{tm.tm_sec}] {text}\n')
        self.st.configure(state ='disabled')
        


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)

    root.mainloop()
    