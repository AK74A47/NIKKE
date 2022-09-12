import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=800
        height=905
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_468=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_468["font"] = ft
        GLabel_468["fg"] = "#333333"
        GLabel_468["justify"] = "center"
        GLabel_468["text"] = "สมัครสมาชิก"
        GLabel_468.place(x=90,y=40,width=182,height=37)

        GLabel_660=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_660["font"] = ft
        GLabel_660["fg"] = "#333333"
        GLabel_660["justify"] = "center"
        GLabel_660["text"] = "ชื่อ"
        GLabel_660.place(x=100,y=130,width=70,height=25)

        GLabel_547=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_547["font"] = ft
        GLabel_547["fg"] = "#333333"
        GLabel_547["justify"] = "center"
        GLabel_547["text"] = "นามสกุล"
        GLabel_547.place(x=330,y=120,width=157,height=43)

        GLabel_5=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_5["font"] = ft
        GLabel_5["fg"] = "#333333"
        GLabel_5["justify"] = "center"
        GLabel_5["text"] = "รหัสสมาชิกอีเมล"
        GLabel_5.place(x=80,y=220,width=221,height=30)

        GLabel_699=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_699["font"] = ft
        GLabel_699["fg"] = "#333333"
        GLabel_699["justify"] = "center"
        GLabel_699["text"] = "เบอร์โทร"
        GLabel_699.place(x=350,y=220,width=115,height=30)

        GLabel_123=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_123["font"] = ft
        GLabel_123["fg"] = "#333333"
        GLabel_123["justify"] = "center"
        GLabel_123["text"] = "รหัสผ่าน"
        GLabel_123.place(x=120,y=330,width=75,height=30)

        GLabel_90=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_90["font"] = ft
        GLabel_90["fg"] = "#333333"
        GLabel_90["justify"] = "center"
        GLabel_90["text"] = "ยืนยัน รหัสผ่าน"
        GLabel_90.place(x=110,y=430,width=147,height=30)

        GButton_345=tk.Button(root)
        GButton_345["bg"] = "#ff4500"
        ft = tkFont.Font(family='Times',size=16)
        GButton_345["font"] = ft
        GButton_345["fg"] = "#000000"
        GButton_345["justify"] = "center"
        GButton_345["text"] = "ยืนยัน"
        GButton_345.place(x=300,y=550,width=145,height=30)
        GButton_345["command"] = self.GButton_345_command

        GLineEdit_192=tk.Entry(root)
        GLineEdit_192["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_192["font"] = ft
        GLineEdit_192["fg"] = "#333333"
        GLineEdit_192["justify"] = "center"
        GLineEdit_192["text"] = "ชื่อ"
        GLineEdit_192.place(x=120,y=170,width=243,height=33)

        GLineEdit_944=tk.Entry(root)
        GLineEdit_944["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_944["font"] = ft
        GLineEdit_944["fg"] = "#333333"
        GLineEdit_944["justify"] = "center"
        GLineEdit_944["text"] = "นามสกุล"
        GLineEdit_944.place(x=380,y=170,width=242,height=32)

        GLineEdit_648=tk.Entry(root)
        GLineEdit_648["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_648["font"] = ft
        GLineEdit_648["fg"] = "#333333"
        GLineEdit_648["justify"] = "center"
        GLineEdit_648["text"] = "Email"
        GLineEdit_648.place(x=120,y=270,width=243,height=33)

        GLineEdit_632=tk.Entry(root)
        GLineEdit_632["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_632["font"] = ft
        GLineEdit_632["fg"] = "#333333"
        GLineEdit_632["justify"] = "center"
        GLineEdit_632["text"] = "เบอร์โทร"
        GLineEdit_632.place(x=380,y=270,width=243,height=34)

        GLineEdit_664=tk.Entry(root)
        GLineEdit_664["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_664["font"] = ft
        GLineEdit_664["fg"] = "#333333"
        GLineEdit_664["justify"] = "center"
        GLineEdit_664["text"] = "รหัสผ่าน"
        GLineEdit_664.place(x=120,y=380,width=502,height=35)

        GLineEdit_215=tk.Entry(root)
        GLineEdit_215["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_215["font"] = ft
        GLineEdit_215["fg"] = "#333333"
        GLineEdit_215["justify"] = "center"
        GLineEdit_215["text"] = "ยืนยันรหัสผ่าน"
        GLineEdit_215.place(x=120,y=480,width=503,height=36)

    def GButton_345_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
