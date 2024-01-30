from tkinter import *

expression = ""


"""
    update expression in the entry box
"""
def press(num):
    global expression
    global equation


    # concatenation of string
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        global equation

        # eval function evaluate the expression
        # and str function convert the result into string
        total = str(eval(expression))
        equation.set(total)

        equation = ""
    except:
        equation.set
        expression = ""
    finally:
        equation = StringVar()

# Function to clear the contents of text entry

def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    gui.geometry("800x500")

    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar()

    # Create the text entry box for showing the expression
    expression_field = Entry(gui, textvariable=equation)

    # using grid method to place widgets
    expression_field.grid(columnspan=6, ipadx=70)

    # placing a button where I want
    button5 = Button(gui, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=5, width=20)
    button5.grid(row=2, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red', 
                    command=lambda: press("+"), height=5, width=20) 
    plus.grid(row=2, column=5) 
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
                    command=lambda: press(2), height=5, width=20) 
    button2.grid(row=2, column=2) 
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
                    command=lambda: press(4), height=5, width=20) 
    button4.grid(row=3, column=0) 
 
    minus = Button(gui, text=' - ', fg='black', bg='red', 
                    command=lambda: press("-"), height=5, width=20) 
    minus.grid(row=3, column=5) 
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
                    command=lambda: press(5), height=5, width=20) 
    button5.grid(row=3, column=2) 
 
    button20 = Button(gui, text=' 7 ', fg='black', bg='red', 
                    command=lambda: press(7), height=5, width=20) 
    button20.grid(row=4, column=0) 
 
    multiply = Button(gui, text=' * ', fg='black', bg='red', 
                    command=lambda: press("*"), height=5, width=20) 
    multiply.grid(row=4, column=5) 
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
                    command=lambda: press(8), height=5, width=20) 
    button8.grid(row=4, column=2)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                    command=lambda: press(9), height=5, width=20) 
    button9.grid(row=4, column=3)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
                    command=lambda: press(0), height=5, width=20) 
    button0.grid(row=5, column=0)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                    command=lambda: press(3), height=5, width=20) 
    button3.grid(row=2, column=3)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=5, width=20) 
    button6.grid(row=3, column=3)
 
    clear = Button(gui, text='clear ', fg='black', bg='red', 
                    command=clear, height=5, width=20) 
    clear.grid(row=5, column=3) 
 
    equal = Button(gui, text=' = ', fg='black', bg='red', 
                    command=equalpress, height=5, width=20) 
    equal.grid(row=5, column=2) 
 
    divide = Button(gui, text=' / ', fg='black', bg='red', 
                    command=lambda: press("/"), height=5, width=20) 
    divide.grid(row=5, column='5') 
 
    Decimal= Button(gui, text='.', fg='black', bg='red', 
                    command=lambda: press('.'), height=5, width=20) 
    Decimal.grid(row=6, column=0) 

    gui.mainloop()