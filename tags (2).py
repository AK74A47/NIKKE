import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_584=tk.Entry(root)
        GLineEdit_584["bg"] = "#01aaed"
        GLineEdit_584["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_584["font"] = ft
        GLineEdit_584["fg"] = "#333333"
        GLineEdit_584["justify"] = "center"
        GLineEdit_584["text"] = "Username/Email"
        GLineEdit_584.place(x=190,y=140,width=197,height=36)

        GLineEdit_108=tk.Entry(root)
        GLineEdit_108["bg"] = "#01aaed"
        GLineEdit_108["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_108["font"] = ft
        GLineEdit_108["fg"] = "#333333"
        GLineEdit_108["justify"] = "center"
        GLineEdit_108["text"] = "Password"
        GLineEdit_108.place(x=190,y=210,width=197,height=36)

        GLabel_24=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_24["font"] = ft
        GLabel_24["fg"] = "#333333"
        GLabel_24["justify"] = "center"
        GLabel_24["text"] = "เข้าสู่ระบบ"
        GLabel_24.place(x=210,y=60,width=162,height=34)

        GButton_394=tk.Button(root)
        GButton_394["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_394["font"] = ft
        GButton_394["fg"] = "#000000"
        GButton_394["justify"] = "center"
        GButton_394["text"] = "ยืนยันเข้าสู่ระบบ"
        GButton_394.place(x=170,y=290,width=242,height=30)
        GButton_394["command"] = self.GButton_394_command

        GButton_602=tk.Button(root)
        GButton_602["activebackground"] = "#e3e3e3"
        GButton_602["activeforeground"] = "#f9f9f9"
        GButton_602["bg"] = "#fbf8f8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_602["font"] = ft
        GButton_602["fg"] = "#080101"
        GButton_602["justify"] = "center"
        GButton_602["text"] = "สมัครสมาชิก"
        GButton_602.place(x=250,y=250,width=86,height=30)
        GButton_602["command"] = self.GButton_602_command

    def GButton_394_command(self):
        print("command")


    def GButton_602_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
