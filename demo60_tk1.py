import tkinter
from tkinter.font import Font
from pprint import pprint
from demo61_counter import Counter, c1

# class Counter:
#     def __init__(self, value):
#         self.value = value
#
#
# c1 = Counter(0)
top = tkinter.Tk()

selector1 = tkinter.IntVar()
selector1.set(1)

x1 = 0
x2 = [0]


def notifier():
    def inner():
        global x1
        x1 += 1
        label.config(text='button1 clicked %d times' % x1, fg='#C0FFEE', bg='#000000')

    inner()
    button2.pack_forget()


def changeText():
    x2[0] += 1
    label.config(text="button2 clicked %d times" % x2[0], fg='#FFC0EE', bg='#000000')


def changeText2():
    c1.value += 1
    label.config(text="button3 clicked %d times" % c1.value, fg='#FFEEC0', bg='#000000')
    button3.pack_forget()


def func1(ev):
    label.config(text="mouse enter into button4")


def func2(ev):
    label.config(text="mouse leave from button4")


def func3(ev):
    label.config(text="button5 left single click")
    print(f"ev={ev}")


def func4(ev):
    label.config(text="button5 scroll double click")


def func5(ev):
    label.config(text="button5 right drag")


def func6(ev):
    label.config(text="cursor at [%d,%d]" % (ev.x, ev.y))


def func7():
    label.config(text="pixel5")


def func8():
    label.config(text="iphone12")


def func7_8():
    if selector1.get() == 1:
        label.config(text="pixel5")
    elif selector1.get() == 2:
        label.config(text="iphone12")


def func9(x):
    label.config(text="volume set to %d" % int(x))


def func10(x):
    label.config(text=entry1.get())


for font in tkinter.font.families():
    pprint(font)

myFont1 = Font(family='Courier', size=24)
myFont2 = Font(family='Liberation Sans', size=24)
label = tkinter.Label(top, text='hello tkinter', font=myFont1, padx=20, bg='#C0FFEE', fg='#550000')
button = tkinter.Button(top, text='button1', font=myFont2, pady=20, fg='#C0FFEE', bg='#004400',
                        command=notifier)
button2 = tkinter.Button(top, text='button2', font=myFont2, pady=20, fg='#FFC0EE', bg='#440000',
                         command=changeText)

button3 = tkinter.Button(top, text='button3', font=myFont2, pady=20, fg='#FFEEC0', bg='#000044',
                         command=changeText2)
button4 = tkinter.Button(top, text='button4', font=myFont2, pady=20, fg='#000044', bg='#FFEEC0', padx=20)
button4.bind('<Leave>', func2)
button4.bind('<Enter>', func1)
button5 = tkinter.Button(top, text='button5', font=myFont2, pady=10, fg='#FFEEC0', bg='#000044', padx=10)
button5.bind('<Button-1>', func3)
button5.bind('<Double-2>', func4)
button5.bind('<B3-Motion>', func5)
label2 = tkinter.Label(top, text="detect cursor area", font=myFont2, padx=20, pady=20,
                       bg='#FFC0EE', fg='#005500')
label2.bind('<Motion>', func6)
## radio button
rb1 = tkinter.Radiobutton(top, text="Android", font=myFont2, value=1, command=func7_8, variable=selector1)
rb2 = tkinter.Radiobutton(top, text="iOS", font=myFont2, value=2, command=func7_8, variable=selector1)
# scale
value1 = tkinter.IntVar()
scale1 = tkinter.Scale(top, label="Volume", orient='h', from_=0, to=100,
                       font=myFont2, variable=value1, command=func9)
entry1 = tkinter.Entry(top, font=myFont2)
button6 = tkinter.Button(top, text="button6/submit", font=myFont2)
entry1.bind('<Return>', func10)
button6.bind('<Button-1>', func10)
label.pack()
entry1.pack()
button6.pack()
scale1.pack()
rb1.pack()
rb2.pack()
label2.pack()
button.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
top.minsize(500, 600)
top.maxsize(500, 600)
top.mainloop()
