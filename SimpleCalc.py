from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Worst Calculator")
root.geometry("225x250")
root.configure(bg="gray")
root.resizable(False, False)

buttonFrame = Frame(root, bg="#bfbfbf")
buttonFrame.pack()

exp = ""
def press(num):
    global exp
    exp = exp + str(num)
    numbers.set(exp)

def equal(num):
    global exp
    sum = str(eval(exp))
    numbers.set(sum)


numbers = StringVar()
numbers.set("0")
values = Entry(buttonFrame, textvariable=numbers, justify=RIGHT, font=('Garamond',12,"bold"), bd="4")
values.grid(columnspan=4, ipadx="10", pady="5")

button1 = Button(buttonFrame, text="1", relief="ridge", bd="1", width=8,height=2,command=lambda:press(1))
button2 = Button(buttonFrame, text="2", relief="ridge", bd="1", width=8,height=2,command=lambda:press(2))
button3 = Button(buttonFrame, text="3", relief="ridge", bd="1", width=8,height=2,command=lambda:press(3))
button4 = Button(buttonFrame, text="4", relief="ridge", bd="1", width=8,height=2,command=lambda:press(4))
button5 = Button(buttonFrame, text="5", relief="ridge", bd="1", width=8,height=2,command=lambda:press(5))
button6 = Button(buttonFrame, text="6", relief="ridge", bd="1", width=8,height=2,command=lambda:press(6))
button7 = Button(buttonFrame, text="7", relief="ridge", bd="1", width=8,height=2,command=lambda:press(7))
button8 = Button(buttonFrame, text="8", relief="ridge", bd="1", width=8,height=2,command=lambda:press(8))
button9 = Button(buttonFrame, text="9", relief="ridge", bd="1", width=8,height=2,command=lambda:press(9))
button0 = Button(buttonFrame, text="0", relief="ridge", bd="1", width=8,height=2,command=lambda:press(0))
buttonAdd = Button(buttonFrame, text="+", relief="ridge", bd="1", width=8,height=2,command=lambda:press("+"))
buttonEqual = Button(buttonFrame, text="=", relief="ridge", bd="1", width=8,height=2,command=lambda:equal("="))


buttonEqual.grid(row=4,column=2)
buttonAdd.grid(row=4,column=1)
button0.grid(row=4, column=0)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

root.mainloop()








