import tkinter as tk 

# config ventana
calculadora = tk.Tk()
calculadora.title("calculadora")
calculadora.geometry("355x350")

# config botones
anchura = 5
altura = 2
fuente = ("Arial",15)


texto_display = ""

def agregar_x(x):
    global texto_display
    texto_display += x
    display.config(text=texto_display)
    
def delete():
    
    global texto_display
    texto_display = texto_display[:-1]
    display.config(text=texto_display)
    
def result():
    global texto_display
    texto_display = str(eval(texto_display))
    display.config(text=texto_display)
    
teclas = [
    ['7', '8', '9' ,"+"],
    ['4', '5', '6' ,"-"],
    ['1', '2', '3' ,"*"],
    ['.', '0', '//',"/"]
]

# pantalla calculadora
display = tk.Label(
    calculadora, 
    bg="#8be6e9",
    height=3,
    border=10,
    relief="sunken",
    text= texto_display
    )
# posicion pantalla calculadora
display.pack(
    fill="x", 
    anchor="n")


# marco botones numeros
marco_botones_numeros = tk.Frame(
    calculadora,
    bg="#496f70"
)
marco_botones_numeros.pack(
    fill="both",
    expand=True
)

# botones

for id_fila, fila_teclas in enumerate(teclas):
    for id_columnas, texto_tecla in enumerate(fila_teclas):
        
        boton = tk.Button(

            marco_botones_numeros,
            text=texto_tecla,
            bg="#496f70",
            height=altura,
            width=anchura,
            font=fuente,
            command = lambda argumento = texto_tecla: agregar_x(argumento)
        )
        boton.grid(row=id_fila, column=id_columnas, padx=3, pady=3) 


boton_delete = tk.Button(
            marco_botones_numeros,
            text="delete",
            bg="#496f70",
            height=altura,
            width=anchura,
            font=fuente,
            command = delete
        )
boton_delete.grid(row=0, column=4, padx=3, pady=3) 

boton_resultado = tk.Button(
            marco_botones_numeros,
            text="=",
            bg="#496f70",
            height=altura,
            width=anchura,
            font=fuente,
            command = result
        )
boton_resultado.grid(row=1, column=4, padx=3, pady=3) 


if len(texto_display) > 5:
    print("texto muy largo")

calculadora.mainloop()