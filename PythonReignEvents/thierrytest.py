from tkinter import *

from tkinter import ttk  # renames to ttk
# import calendar module
import calendar


class main:
    def __init__(self, master):
        self.master = master
        self.month = IntVar()
        self.year = IntVar(value=2018)
        self.months = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        self.widgets()

    def getcal(self):
        m = self.month.get()
        y = self.year.get()
        cal = calendar.month(y, m, 2, 1)
        self.area.delete(0.0, END)
        self.area.insert(0.0, cal)

    def widgets(self):  # widgets of the calendar drop

        # Label of the calendar and padding, font, frame etc
        Label(self.master, text='Calendar', font=('timesnewroman', 30), bd=10).pack()
        f = Frame(self.master, pady=10, padx=10)

        # Label and entry for month
        Label(f, text='Month: ', font=('freesansbold', 13)).grid()
        mon = ttk.Combobox(f, width=7, font=('freesansbold', 13), values=self.months, textvariable=self.month)
        mon.grid(row=0, column=1)
        mon.current(0)

        # Label and entry for year
        Label(f, text='Year: ', font=('freesansbold', 13)).grid(row=0, column=2)
        ttk.Entry(f, width=9, font=('freesansbold', 13), textvariable=self.year).grid(row=0, column=3)
        f.pack()
        self.area = Text(self.master, font=('', 20), width=20, height=7, bd=15)
        self.area.pack()

        # button set to the getcal function
        Button(self.master, command=self.getcal, text='Get calendar', font=('', 15, 'bold'), bd=10).pack()


if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Calendar')
    root.mainloop()
