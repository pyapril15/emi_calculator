"""
Loan Calculations
When you take out a loan, you must pay back the loan plus interest by making regular payments to the bank.
So you can think of a loan as an annuity you pay to a lending institution.
For loan calculations we can use the formula for the Present Value of an Ordinary Annuity:

PV=(PMT/i)(1−(1/(1+i)^n))
PV is the loan amount
PMT is the monthly payment
i is the interest rate per month in decimal form (interest rate percentage divided by 12)
n is the number of months (term of the loan in months)
"""

from tkinter import *
from tkinter import ttk
from math import log


def validate_input_int(input_int):
    if input_int.replace('.', '').isdigit():
        return True
    if input_int == "":
        return True
    else:
        return False


class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('350x200+450+150')
        self.root.title('EMI Calculator')
        self.root.resizable(width=False, height=False)
        self.root.iconbitmap('./image/emi-calculator.ico')

        self.choice = StringVar(self.root)
        self.i = StringVar()  # interest Rate
        self.pv = StringVar()  # loan amount
        self.pmt = StringVar()  # monthly payment
        self.n = StringVar()  # no of month

        self.frame = Frame(self.root)
        self.frame.pack(side=TOP, fill=BOTH, padx=5, pady=5)

        self.label = Label(self.frame, text='Choose Your Calculation', font=('sanserif', 13, "bold"))
        self.label.pack(side=TOP, padx=5)

        self.combo = ttk.Combobox(self.frame, width=22, textvariable=self.choice, font=('sanserif', 12), cursor="hand2",
                                  state="readonly")
        self.combo['values'] = (
            'Find the Loan Amount',
            'Find the Simple Interest',
            'Find the numbers of Month',
            'Find the Monthly Payment'
        )
        self.combo.pack(side=TOP, padx=5)
        self.combo.current(0)

        self.canvas = Canvas(self.frame)
        self.canvas.pack(side=TOP, fill=BOTH, padx=5, pady=10)

        self.left_canvas = Canvas(self.canvas)
        self.left_canvas.pack(side=LEFT, padx=2, pady=2)

        self.right_canvas = Canvas(self.canvas)
        self.right_canvas.pack(side=RIGHT)

        self.i_lbl = Label(self.left_canvas, text='Interest rate', font=('sanserif', 13))
        self.i_lbl.pack(side=TOP, padx=5, anchor=W)
        self.i_ent = Entry(self.right_canvas, textvariable=self.i, font=('sanserif', 13))
        self.i_ent.pack(side=TOP, padx=5, pady=3, anchor=W)
        validate = self.root.register(validate_input_int)
        self.i_ent.config(validate='key', validatecommand=(validate, '%P'))

        self.n_lbl = Label(self.left_canvas, text='Number of Months', font=('sanserif', 13))
        self.n_lbl.pack(side=TOP, padx=5, anchor=W)
        self.n_ent = Entry(self.right_canvas, textvariable=self.n, font=('sanserif', 13))
        self.n_ent.pack(side=TOP, padx=5, pady=3, anchor=W)
        validate = self.root.register(validate_input_int)
        self.n_ent.config(validate='key', validatecommand=(validate, '%P'))

        self.pmt_lbl = Label(self.left_canvas, text='Monthly Payment', font=('sanserif', 13))
        self.pmt_lbl.pack(side=TOP, padx=5, anchor=W)
        self.pmt_ent = Entry(self.right_canvas, textvariable=self.pmt, font=('sanserif', 13))
        self.pmt_ent.pack(side=TOP, padx=5, pady=3, anchor=W)
        validate = self.root.register(validate_input_int)
        self.pmt_ent.config(validate='key', validatecommand=(validate, '%P'))

        self.combo.bind("<<ComboboxSelected>>", self.display)

        self.btn = Button(self.frame, text='Clear', font=("", 11, "bold"), cursor="hand2", bd=0, bg='light grey',
                          command=self.clear)
        self.btn.pack(side=LEFT, padx=25)

        self.entry = Entry(self.frame, textvariable=self.pv, font=('sanserif', 13), width=13, state='readonly')
        self.entry.pack(side=LEFT, pady=3, anchor=CENTER)

        self.btn = Button(self.frame, text='Calculate', font=("", 11, "bold"), cursor="hand2", bg='light grey', bd=0,
                          command=self.result)
        self.btn.pack(side=RIGHT, padx=25)

    def display(self, event):
        if self.choice.get() == 'Find the Loan Amount':
            self.clear()
            self.i_lbl.config(text='Interest Rate')
            self.i_ent.config(textvariable=self.i)
            self.n_lbl.config(text='Number of Months')
            self.n_ent.config(textvariable=self.n)
            self.pmt_lbl.config(text='Monthly Payment')
            self.pmt_ent.config(textvariable=self.pmt)
            self.entry.config(textvariable=self.pv)

        if self.choice.get() == 'Find the Simple Interest':
            self.clear()
            self.i_lbl.config(text='Interest Rate')
            self.i_ent.config(textvariable=self.i)
            self.n_lbl.config(text='Number of Year')
            self.n_ent.config(textvariable=self.n)
            self.pmt_lbl.config(text='Principal Amount')
            self.pmt_ent.config(textvariable=self.pmt)
            self.entry.config(textvariable=self.pv)

        if self.choice.get() == 'Find the numbers of Month':
            self.clear()
            self.i_lbl.config(text='Interest Rate')
            self.i_ent.config(textvariable=self.i)
            self.n_lbl.config(text='Loan Amount')
            self.n_ent.config(textvariable=self.pv)
            self.pmt_lbl.config(text='Monthly Payment')
            self.pmt_ent.config(textvariable=self.pmt)
            self.entry.config(textvariable=self.n)

        if self.choice.get() == 'Find the Monthly Payment':
            self.clear()
            self.i_lbl.config(text='Interest Rate')
            self.i_ent.config(textvariable=self.i)
            self.n_lbl.config(text='Number of Months')
            self.n_ent.config(textvariable=self.n)
            self.pmt_lbl.config(text='Loan Amount')
            self.pmt_ent.config(textvariable=self.pv)
            self.entry.config(textvariable=self.pmt)

    def validate(self):
        if self.choice.get() == 'Find the Loan Amount':
            val = bool(self.i.get() and self.n.get() and self.pmt.get())
            if val:
                return True

        if self.choice.get() == 'Find the Simple Interest':
            val = bool(self.i.get() and self.n.get() and self.pmt.get())
            if val:
                return True

        if self.choice.get() == 'Find the numbers of Month':
            val = bool(self.pv.get() and self.i.get() and self.pmt.get())
            if val:
                return True

        if self.choice.get() == 'Find the Monthly Payment':
            val = bool(self.pv.get() and self.n.get() and self.i.get())
            if val:
                return True

    def result(self):
        if self.choice.get() == 'Find the Loan Amount':
            if self.validate():
                try:
                    pmt = int(self.pmt.get())
                    i = (float(self.i.get())) / 1200
                    n = int(self.n.get())
                    loan_amount = ((pmt / i) * (1 - (1 / (1 + i) ** n)))
                    loan_amount = round(loan_amount, 2)
                    self.pv.set(loan_amount)
                except:
                    pass
            else:
                self.entry.config(fg='red', font=('sanserif', 10), width=17)
                self.pv.set('All input are required')

        if self.choice.get() == 'Find the Simple Interest':
            if self.validate():
                try:
                    p = float(self.pmt.get())
                    r = float(self.i.get()) / 100
                    t = float(self.n.get())
                    t = round(t, 2)
                    a = p * (1 + r * t)
                    interest = round(a - p, 2)
                    self.pv.set(interest)
                except:
                    pass
            else:
                self.entry.config(fg='red', font=('sanserif', 10), width=17)
                self.pv.set('All input are required')

        if self.choice.get() == 'Find the numbers of Month':
            if self.validate():
                try:
                    pmt = int(self.pmt.get())
                    i = (float(self.i.get())) / 1200
                    loan_amount = float(self.pv.get())
                    sol_1 = ((pmt / i) / ((pmt / i) - loan_amount))
                    sol_2 = 1 + i
                    n = log(sol_1) / log(sol_2)
                    n = round(n)
                    self.n.set(n)
                except:
                    self.entry.config(fg='red', font=('sanserif', 10), width=17)
                    self.n.set('Cannot be predicted')
            else:
                self.entry.config(fg='red', font=('sanserif', 10), width=17)
                self.n.set('All input are required')

        if self.choice.get() == 'Find the Monthly Payment':
            if self.validate():
                try:
                    loan_amount = float(self.pv.get())
                    i = (float(self.i.get())) / 1200
                    n = int(self.n.get())
                    pmt = (((loan_amount * i) * (1 + i) ** n) / ((1 + i) ** n - 1))
                    pmt = round(pmt, 2)
                    self.pmt.set(pmt)
                except:
                    pass
            else:
                self.entry.config(fg='red', font=('sanserif', 10), width=17)
                self.pmt.set('All input are required')

    def clear(self):
        self.pv.set('')
        self.pmt.set('')
        self.i.set('')
        self.n.set('')
        self.entry.config(font=('sanserif', 13), width=13)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    win = App()
    win.run()
