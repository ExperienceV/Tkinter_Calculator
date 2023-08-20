from tkinter import *

window = Tk()
window.title("Calculadora")
window["background"] = "#B6C8F3"


# Input
in_text = Entry(window, font=("Calibri 20"), bg="#F4ECF7")
in_text.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Funciones
i = 0  # Variable para realizar seguimiento de la posición en la entrada

def click_butt(value):
    global i
    in_text.insert(i, value)
    i += 1

def delete():
    global i
    in_text.delete(0, END)
    i = 0

def result():
    global i
    ecuacion = in_text.get()
    r = eval(ecuacion)
    in_text.delete(0, END)
    in_text.insert(0, r)
    i = 0

# Button_Operations
button_labels = [
    ["AC", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", " "]
]

buttons = []

for row, label_row in enumerate(button_labels):
    button_row = []
    for col, label in enumerate(label_row):
        if label == " ":
            button = Label(window, text="", bg="#B6C8F3", height=2, width=5)
        else:
            button = Button(window, text=label, bg="#E8DAEF", height=2, width=5, command=lambda value=label: click_butt(value))
            if label == "AC":
                button.config(command=delete)
            elif label == "=":
                button.config(command=result)
        button.grid(row=row + 1, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

window.mainloop()
