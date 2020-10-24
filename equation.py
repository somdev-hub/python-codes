from tkinter import *
import math
from tkinter import font

'''GUI program that calculates the roots of a quadratic equation that is in the form of AX^2+BX+C=0'''


def click3():
    try:
        value1 = int(b_input.get())
        value2 = int(a_input.get())
        value3 = int(c_input.get())
        r = (value1 * value1) - (4 * value2 * value3)

        if r > 0:
            x_value = (-value1 + math.sqrt(r)) / (2 * value2)
            y_value = (-value1 - math.sqrt(r)) / (2 * value2)
            text1_var.set(x_value)
            text2_var.set(y_value)
            root1_input.update()
            root2_input.update()

        elif r == 0:
            z_value = (-value1) / (2 * value2)
            text1_var.set(z_value)
            text2_var.set(z_value)
            root1_input.update()
            root2_input.update()

        else:
            text1_var.set("roots are complicated")
            text2_var.set("roots are complicated")
            root1_input.update()
            root2_input.update()

    except Exception as error:
        print(error)
        text1_var.set("error")
        text2_var.set("error")
        root1_input.update()
        root2_input.update()


# __MAIN__

root = Tk()
root.iconbitmap(r'C:\Users\hello\Downloads\favicon_io\favicon.ico')
root.title("quadratic equation")
root.config(bg="light green")
Font1 = font.Font(family="ariel", size=10, weight="bold")
text1_var = StringVar()
text2_var = StringVar()

# __labels__

label1 = Label(root, text="enter the value of a", bg="light green", font=Font1)
label2 = Label(root, text="enter the value of b", bg="light green", font=Font1)
label3 = Label(root, text="enter the value of c", bg="light green", font=Font1)
label_r = Label(root, bg="light green", text="the roots are", font=Font1)

# __entries__

a_input = Entry(root, width=20, borderwidth=5, font=Font1, bg="wheat1")
b_input = Entry(root, width=20, borderwidth=5, font=Font1, bg="wheat1")
c_input = Entry(root, width=20, borderwidth=5, font=Font1, bg="wheat1")
root1_input = Entry(root, width=8, borderwidth=5, font=Font1, textvar=text1_var, bg="wheat1")
root2_input = Entry(root, width=8, borderwidth=5, font=Font1, textvar=text2_var, bg="wheat1")

# __buttons__

button1 = Button(root, text="CALCULATE", font=Font1, command=click3, bg="gold")

# __griding__

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label_r.grid(row=4, column=0)

a_input.grid(row=0, column=1, columnspan=2)
b_input.grid(row=1, column=1, columnspan=2)
c_input.grid(row=2, column=1, columnspan=2)
root1_input.grid(row=4, column=1)
root2_input.grid(row=4, column=2)

button1.grid(row=3, column=1, columnspan=2)

# __loops starts__

root.mainloop()
