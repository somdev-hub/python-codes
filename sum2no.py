from tkinter import *

"""A simple GUI program that takes two numbers as input from the user and evaluate the sum of the numbers and returns 
the sum in another entry widget """

y_value = 0
x_value = ""


def click2():  # defining function
    global y_value, x_value
    try:
        value1 = int(s_input.get())
        value2 = int(t_input.get())
        y_value = value1 + value2
        x_value = str(y_value)

    except Exception as e:
        print(e)
        x_value = "error"

    value.set(x_value)
    result.update()


# __main structure__

root = Tk()
root.title("GUI sum")
root.config(bg="yellow")
value = StringVar()

label1 = Label(root, text="enter 1st number:", bg="yellow")
label2 = Label(root, text="enter 2nd number:", bg="yellow")
label3 = Label(root, text="result :", bg="yellow")

s_input = Entry(root, width=20, borderwidth=5, bg="pink")
t_input = Entry(root, width=20, borderwidth=5, bg="pink")
result = Entry(root, textvar=value, width=20, borderwidth=5, bg="pink")

button1 = Button(root, text="sum", padx=45, pady=3, bg="cyan", command=click2)

s_input.grid(row=1, column=2)
t_input.grid(row=3, column=2)
result.grid(row=5, column=2)

label1.grid(row=1, column=1)
label2.grid(row=3, column=1)
label3.grid(row=5, column=1)

button1.grid(row=4, column=2)

# loop starts

root.mainloop()
