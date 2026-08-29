import numpy as np
import tkinter as tk 
from random import randint

sudoku_botones = tk.Tk()
sudoku_botones.title("sudoku parametros")

marco_sudoku = tk.Frame(
    sudoku_botones,
    bg="#496f70"
)
marco_sudoku.pack(
    expand=True,
    fill="both"
)

def cambiar_numero(i_f,i_c):
    numero_b = botones_diccionario[f"{i_f},{i_c}"].cget("text")
    numero_b += 1
    if numero_b > 9:
        numero_b = 0
        
    botones_diccionario[f"{i_f},{i_c}"].config(text=numero_b)
    
def terminar_test():
    sudoku_botones.quit()

botones_diccionario = {}



for id_fila in range(9):
    for id_columna in range(9):
        boton = tk.Button(
            marco_sudoku,
            bg="#54b3b6",
            text=0,
            height=3,
            width=4,
            command= lambda f= id_fila, c= id_columna: cambiar_numero(f,c)
        )

        boton.grid(row=id_fila, column=id_columna,padx=2, pady=2) 

        botones_diccionario[f"{id_fila},{id_columna}"] = boton

boton_test= tk.Button(
    sudoku_botones,
    bg="#AC0909",
    text="subir marco",
    command= terminar_test,
    )
boton_test.pack(
    fill="x"
)

sudoku_botones.mainloop()


estructura_prueba = []
lista_temporal = []

for id_fila, _ in enumerate(range(1,10)):
    
    for id_columna, _ in enumerate(range(1,10)):
        
        
        lista_temporal.append(botones_diccionario[f"{id_fila},{id_columna}"].cget("text"))

    estructura_prueba.append(lista_temporal)
    lista_temporal = []



tablero = np.array(estructura_prueba)

def encontrar_posicion_vacia(tablero):
    for index_f in range(9):
        for index_c in range(9):
            if tablero[index_f,index_c] == 0:
                return tuple([index_f,index_c])
    return False
            
def es_valido(tablero,index_f,index_c,insertar):
    inicio_f = index_f - index_f % 3
    inicio_c = index_c - index_c % 3
    bloque_3x3 = tablero[inicio_f:inicio_f + 3, inicio_c:inicio_c + 3]
    if (not np.any(tablero[index_f] == insertar)) and \
        (not np.any(tablero[:,index_c] == insertar)) and \
        (not np.any(bloque_3x3 == insertar)):
        return True
    return False

def resolver_sudoku(tablero):
    posicion_vacia = encontrar_posicion_vacia(tablero)
    
    if not posicion_vacia:
        return True
    
    index_f,index_c = encontrar_posicion_vacia(tablero)

    for num in range (1,10):
        insertar = num
        if es_valido(tablero, index_f, index_c, insertar):
            tablero[index_f, index_c] = insertar
            if resolver_sudoku(tablero):
                return True
                
            tablero[index_f, index_c] = 0  
                
    return False


resolver_sudoku(tablero)

print(tablero)

sudoku_resultado = tk.Tk()
sudoku_resultado.title("sudoku resultados")

marco_resultado = tk.Frame(
    sudoku_resultado,
    bg="#496f70"
)
marco_resultado.pack(
    expand=True,
    fill="both"
)
for id_fila in range(9):
    for id_columna in range(9):
        boton = tk.Button(
            marco_resultado,
            bg="#54b3b6",
            text= tablero[id_fila][id_columna],
            height=3,
            width=4,
        )
        boton.grid(row=id_fila, column=id_columna,padx=2, pady=2) 
        
sudoku_resultado.mainloop()






