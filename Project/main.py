from tkinter import *
from tkinter import ttk

def che(text, repeats, dots, symbol):
    result = ""
    for _ in range(repeats):
        for i in range(dots):
            result += symbol * i + text + "\n"
        for i in range(dots, 0, -1):
            result += symbol * i + text + "\n"
    return result


def generate_text():
    text = tl1.get()
    repeats = int(tl2.get())
    dots = int(tl3.get())
    symbol = tl4.get()

    result_text = che(text, repeats, dots, symbol)

    tlresult.config(state="normal")
    tlresult.delete(1.0, END)
    tlresult.insert(END, result_text)
    tlresult.config(state="disabled")


root = Tk()
root.title("DotClick")
root.geometry("300x430")

tl1 = ttk.Entry(root, width=30)
tl2 = ttk.Entry(root, width=30)
tl3 = ttk.Entry(root, width=30)
tl4 = ttk.Entry(root, width=30)
tlresult = Text(root, height=20, width=50)
btn = ttk.Button(root, text="Генерация", width=430, command=generate_text)

tl1.pack()
tl2.pack()
tl3.pack()
tl4.pack()
tlresult.pack()
btn.pack()

root.mainloop()