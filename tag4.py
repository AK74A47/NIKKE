import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1050
        height=495
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_321=tk.Listbox(root)
        GListBox_321["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_321["font"] = ft
        GListBox_321["fg"] = "#333333"
        GListBox_321["justify"] = "center"
        GListBox_321.place(x=10,y=20,width=832,height=452)

        GLabel_604=tk.Label(root)
        GLabel_604["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=28)
        GLabel_604["font"] = ft
        GLabel_604["fg"] = "#333333"
        GLabel_604["justify"] = "center"
        GLabel_604["text"] = "ตะกร้าสินค้า"
        GLabel_604.place(x=20,y=40,width=172,height=31)

        GListBox_849=tk.Listbox(root)
        GListBox_849["borderwidth"] = "1px"
        GListBox_849["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_849["font"] = ft
        GListBox_849["fg"] = "#333333"
        GListBox_849["justify"] = "center"
        GListBox_849.place(x=510,y=100,width=294,height=341)

        GLabel_56=tk.Label(root)
        GLabel_56["activebackground"] = "#ffffff"
        GLabel_56["activeforeground"] = "#ffffff"
        GLabel_56["bg"] = "#ffffff"
        GLabel_56["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_56["font"] = ft
        GLabel_56["fg"] = "#333333"
        GLabel_56["justify"] = "center"
        GLabel_56["text"] = "สรุปการสั่งซื้อ"
        GLabel_56.place(x=520,y=110,width=127,height=32)

        GLabel_704=tk.Label(root)
        GLabel_704["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_704["font"] = ft
        GLabel_704["fg"] = "#333333"
        GLabel_704["justify"] = "center"
        GLabel_704["text"] = "ราคา"
        GLabel_704.place(x=520,y=150,width=70,height=25)

        GLabel_983=tk.Label(root)
        GLabel_983["activebackground"] = "#ffffff"
        GLabel_983["activeforeground"] = "#ffffff"
        GLabel_983["bg"] = "#ffffff"
        GLabel_983["disabledforeground"] = "#fefefe"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_983["font"] = ft
        GLabel_983["fg"] = "#393d49"
        GLabel_983["justify"] = "center"
        GLabel_983["text"] = "ส่วนลด"
        GLabel_983.place(x=520,y=180,width=90,height=30)

        GLabel_391=tk.Label(root)
        GLabel_391["activebackground"] = "#ffffff"
        GLabel_391["activeforeground"] = "#fcfcfc"
        GLabel_391["bg"] = "#ffffff"
        GLabel_391["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_391["font"] = ft
        GLabel_391["fg"] = "#333333"
        GLabel_391["justify"] = "center"
        GLabel_391["text"] = "0 .-"
        GLabel_391.place(x=630,y=150,width=84,height=30)

        GListBox_831=tk.Listbox(root)
        GListBox_831["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_831["font"] = ft
        GListBox_831["fg"] = "#333333"
        GListBox_831["justify"] = "center"
        GListBox_831.place(x=540,y=220,width=121,height=30)

        GButton_616=tk.Button(root)
        GButton_616["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=12)
        GButton_616["font"] = ft
        GButton_616["fg"] = "#000000"
        GButton_616["justify"] = "center"
        GButton_616["text"] = "ใช้"
        GButton_616.place(x=680,y=220,width=72,height=30)
        GButton_616["command"] = self.GButton_616_command

        GLabel_280=tk.Label(root)
        GLabel_280["activebackground"] = "#ffffff"
        GLabel_280["activeforeground"] = "#fbf7f7"
        GLabel_280["bg"] = "#ffffff"
        GLabel_280["disabledforeground"] = "#f9f9f9"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_280["font"] = ft
        GLabel_280["fg"] = "#333333"
        GLabel_280["justify"] = "center"
        GLabel_280["text"] = "ยอดสุทธิ"
        GLabel_280.place(x=530,y=260,width=89,height=30)

        GLabel_616=tk.Label(root)
        GLabel_616["activebackground"] = "#f9f9f9"
        GLabel_616["activeforeground"] = "#fbfbfb"
        GLabel_616["bg"] = "#ffffff"
        GLabel_616["disabledforeground"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_616["font"] = ft
        GLabel_616["fg"] = "#333333"
        GLabel_616["justify"] = "center"
        GLabel_616["text"] = "0.-"
        GLabel_616.place(x=640,y=260,width=70,height=25)

        GButton_966=tk.Button(root)
        GButton_966["bg"] = "#35c14d"
        ft = tkFont.Font(family='Times',size=14)
        GButton_966["font"] = ft
        GButton_966["fg"] = "#fffafa"
        GButton_966["justify"] = "center"
        GButton_966["text"] = "ดำเนินการต่อ"
        GButton_966.place(x=540,y=310,width=213,height=41)
        GButton_966["command"] = self.GButton_966_command

        GButton_895=tk.Button(root)
        GButton_895["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=14)
        GButton_895["font"] = ft
        GButton_895["fg"] = "#5fb878"
        GButton_895["justify"] = "center"
        GButton_895["text"] = "เลือกสินค้าต่อ"
        GButton_895.place(x=540,y=370,width=212,height=41)
        GButton_895["command"] = self.GButton_895_command

        GLabel_156=tk.Label(root)
        GLabel_156["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_156["font"] = ft
        GLabel_156["fg"] = "#333333"
        GLabel_156["justify"] = "left"
        GLabel_156["text"] = "คุณไม่มีสินค้าในตะกร้า"
        GLabel_156.place(x=30,y=100,width=415,height=36)


    def GButton_616_command(self):
        print("command")


    def GButton_966_command(self):
        print("command")


    def GButton_895_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
