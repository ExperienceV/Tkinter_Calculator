# Importar la biblioteca Tkinter
from tkinter import *

# Crear la ventana principal
window = Tk()

# Establecer el color de fondo de la ventana principal
window["background"] = "#B6C8F3"

# Crear un campo de entrada (input) para la calculadora
in_text = Entry(window, font=("Calibri 20"), bg="#F4ECF7")
in_text.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Variable para realizar seguimiento de la posición en la entrada
i = 0

# Función para manejar el click en los botones numéricos y de operación
def click_butt(value):
    global i
    in_text.insert(i, value)  # Insertar el valor en la posición actual
    i += 1

# Función para borrar la entrada y reiniciar la posición
def delete():
    global i
    in_text.delete(0, END)  # Borrar todo el contenido
    i = 0

# Función para calcular y mostrar el resultado
def result():
    global i
    ecuacion = in_text.get()  # Obtener el contenido del campo de entrada
    r = eval(ecuacion)  # Calcular el resultado usando eval
    in_text.delete(0, END)  # Borrar todo el contenido
    in_text.insert(0, r)  # Insertar el resultado en el campo
    i = 0

# Definir las etiquetas de los botones de la calculadora
button_labels = [
    ["AC", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", " "]
]

# Crear una matriz de botones y etiquetas en un bucle
buttons = []
for row, label_row in enumerate(button_labels):
    button_row = []
    for col, label in enumerate(label_row):
        if label == " ":
            # Crear una etiqueta en blanco
            button = Label(window, text="", bg="#B6C8F3", height=2, width=5)
        else:
            # Crear un botón con el texto y color correspondiente
            button = Button(window, text=label, bg="#E8DAEF", height=2, width=5, command=lambda value=label: click_butt(value))
            # Configurar el comando del botón basado en su etiqueta
            if label == "AC":
                button.config(command=delete)
            elif label == "=":
                button.config(command=result)
        # Colocar el botón en la ventana
        button.grid(row=row + 1, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()
