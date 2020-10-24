import tkinter.font as font
from tkinter import *  # importing tkinter module
from math import *


def click(event):  # defining applicable function
    text = event.widget.cget("text")

    if text == "=":
        """when = is pressed the expression will be evaluated """
        if fvalue.get().isdigit():
            value = int(fvalue.get())
        else:
            try:
                value = eval(input_field.get())
            except Exception as error:
                print(error)
                value = "Error"

        fvalue.set(value)
        input_field.update()

    elif text == "clear":
        """when clear is pressed the input field will be reset """
        fvalue.set("")
        input_field.update()
    else:
        fvalue.set(fvalue.get() + text)
        input_field.update()


# __main__

root = Tk()
root.iconbitmap(r'C:\Users\hello\Downloads\favicon_io\favicon.ico')
Font1 = font.Font(family="Times", size=15, weight="bold")
root.config(bg="wheat1")
fvalue = StringVar()
fvalue.set("")
root.title('scientific calculator by Programmer Foundation')
input_field = Entry(root, textvar=fvalue, width=20, borderwidth=5, bg="AntiqueWhite1", font=Font1)
input_field.grid(row=0, column=2, columnspan=3, padx=20, pady=10)

# __creating buttons__

# numeral buttons

button1 = Button(root, text="1", padx=40, pady=20, bg="MistyRose2", font=Font1)
button2 = Button(root, text="2", padx=55, pady=20, bg="MistyRose2", font=Font1)
button3 = Button(root, text="3", padx=45, pady=20, bg="MistyRose2", font=Font1)
button4 = Button(root, text="4", padx=40, pady=20, bg="MistyRose2", font=Font1)
button5 = Button(root, text="5", padx=55, pady=20, bg="MistyRose2", font=Font1)
button6 = Button(root, text="6", padx=45, pady=20, bg="MistyRose2", font=Font1)
button7 = Button(root, text="7", padx=40, pady=20, bg="MistyRose2", font=Font1)
button8 = Button(root, text="8", padx=55, pady=20, bg="MistyRose2", font=Font1)
button9 = Button(root, text="9", padx=45, pady=20, bg="MistyRose2", font=Font1)
button0 = Button(root, text="0", padx=55, pady=20, bg="MistyRose2", font=Font1)

# operator buttons

button_plus = Button(root, text="+", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_minus = Button(root, text="-", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_into = Button(root, text="*", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_divide = Button(root, text="/", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_equal = Button(root, text="=", padx=40, pady=20, bg="MistyRose2", font=Font1)
button_clear = Button(root, text="clear", padx=25, pady=20, bg="MistyRose2", font=Font1)
button_point = Button(root, text=".", padx=45, pady=20, bg="MistyRose2", font=Font1)
button_two_zero = Button(root, text="00", padx=45, pady=20, bg="MistyRose2", font=Font1)

button_sin = Button(root, text="sin", padx=55, pady=20, bg="MistyRose2", font=Font1)
button_cos = Button(root, text="cos", padx=55, pady=20, bg="MistyRose2", font=Font1)
button_tan = Button(root, text="tan", padx=55, pady=20, bg="MistyRose2", font=Font1)
button_br1 = Button(root, text="(", padx=65, pady=20, bg="MistyRose2", font=Font1)
button_br2 = Button(root, text=")", padx=65, pady=20, bg="MistyRose2", font=Font1)

button_sqrt = Button(root, text="sqrt", padx=41, pady=20, bg="MistyRose2", font=Font1)
button_exp = Button(root, text="exp", padx=43, pady=20, bg="MistyRose2", font=Font1)
button_log10 = Button(root, text="log10", padx=35, pady=20, bg="MistyRose2", font=Font1)
button_pi = Button(root, text="pi", padx=50, pady=20, bg="MistyRose2", font=Font1)
button_fac = Button(root, text="factorial", padx=21, pady=20, bg="MistyRose2", font=Font1)

# __binding buttons__

button1.grid(row=1, column=1)
button1.bind("<Button-1>", click)
button2.grid(row=1, column=2)
button2.bind("<Button-1>", click)
button3.grid(row=1, column=3)
button3.bind("<Button-1>", click)

button4.grid(row=2, column=1)
button4.bind("<Button-1>", click)
button5.grid(row=2, column=2)
button5.bind("<Button-1>", click)
button6.grid(row=2, column=3)
button6.bind("<Button-1>", click)

button7.grid(row=3, column=1)
button7.bind("<Button-1>", click)
button8.grid(row=3, column=2)
button8.bind("<Button-1>", click)
button9.grid(row=3, column=3)
button9.bind("<Button-1>", click)

button0.grid(row=4, column=2)
button0.bind("<Button-1>", click)

button_plus.grid(row=0, column=5)
button_plus.bind("<Button-1>", click)
button_minus.grid(row=1, column=5)
button_minus.bind("<Button-1>", click)
button_into.grid(row=2, column=5)
button_into.bind("<Button-1>", click)
button_divide.grid(row=3, column=5)
button_divide.bind("<Button-1>", click)
button_two_zero.grid(row=4, column=5)
button_two_zero.bind("<Button-1>", click)

button_equal.grid(row=4, column=1)
button_equal.bind("<Button-1>", click)
button_clear.grid(row=0, column=1)
button_clear.bind("<Button-1>", click)
button_point.grid(row=4, column=3)
button_point.bind("<Button-1>", click)

button_sin.grid(row=0, column=6)
button_sin.bind("<Button-1>", click)
button_cos.grid(row=1, column=6)
button_cos.bind("<Button-1>", click)
button_tan.grid(row=2, column=6)
button_tan.bind("<Button-1>", click)
button_br1.grid(row=3, column=6)
button_br1.bind("<Button-1>", click)
button_br2.grid(row=4, column=6)
button_br2.bind("<Button-1>", click)

button_sqrt.grid(row=0, column=0)
button_sqrt.bind("<Button-1>", click)
button_exp.grid(row=1, column=0)
button_exp.bind("<Button-1>", click)
button_log10.grid(row=2, column=0)
button_log10.bind("<Button-1>", click)
button_pi.grid(row=3, column=0)
button_pi.bind("<Button-1>", click)
button_fac.grid(row=4, column=0)
button_fac.bind("<Button-1>", click)

# __running mainloop__

root.mainloop()
