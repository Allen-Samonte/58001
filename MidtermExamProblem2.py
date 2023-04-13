from tkinter import *
class MyWindow:
    def __init__(self, win):

#widgets start from here
        self.lbl0 = Label(win, text="My Full Name")
        self.lbl0.place(x=250, y=20)
        self.lbl1 = Label(win, text="Enter Given Name:")
        self.lbl1.place(x=150, y=50)
        self.lbl2 = Label(win, text= "Enter Middle Name:")
        self.lbl2.place(x=150, y=80)
        self.lbl3 = Label(win, text="Enter Last Name:")
        self.lbl3.place(x=150, y=110)
        self.lbl4 = Label(win, text="My Full Name is:")
        self.lbl4.place(x=150, y=150)
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=300, y=50)
        self.txt2 = Entry(win, bd=2)
        self.txt2.place(x=300, y=80)
        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=300, y=110)
        self.txt4 = Entry(win, bd=4, width=30)
        self.txt4.place(x=300, y=150)


        self.btnname = Button(win, text="Show Full Name", command=self.name)
        self.btnname.place(x=250, y=180)

    def name(self):
        self.txt4.delete(0, 'end')
        name1 = self.txt1.get()
        name2 = self.txt2.get()
        name3 = self.txt3.get()
        result = (f"{name1}  {name2}  {name3}")
        self.txt4.insert(END, str(result))

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()