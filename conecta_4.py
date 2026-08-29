import numpy as np
import tkinter as tk 
                    
conecta_4 = tk.Tk()
conecta_4.title("conecta_4")
conecta_4.geometry("400x350")


columna = tk.IntVar(value=9)

estructura_vacia = np.zeros((6,7),dtype=int,order="C") 

fuente = ("Arial",15)

display = tk.Label(
    conecta_4,
    font= fuente,
    text= estructura_vacia,
    bg="#8be6e9"
    
)

display.pack(
    fill="both"
)
marco_botones_numeros = tk.Frame(
    conecta_4,
    bg="#8be6e9"
)
marco_botones_numeros.pack(
    anchor=tk.CENTER,
    expand=False

)


def agregar_x(x):
    global columna
    columna.set(x - 1)


teclas = [1,2,3,4,5,6,7]

for id_columna, tecla in enumerate(teclas):
    
    boton = tk.Button(
        marco_botones_numeros,
        text=tecla,
        font= fuente,
        command= lambda argumento = tecla: agregar_x(argumento)
        
    )
    boton.grid(row=0, column=id_columna)     

def encontrar_fichas(tablero):
    coordendas_desorganizadas = np.where((tablero == 1)|(tablero == 2))
    lista_coordendas = list(zip(coordendas_desorganizadas[0],
                                coordendas_desorganizadas[1]))
    if len(lista_coordendas) == 0:
        return False
    
    return lista_coordendas



def encontrar_4(tablero,index_list):

    
    lista_valores = [(0,0,1,4,"N","U"),
                     (0,3,1,1,"N","U"),
                     (3,0,1,1,"N","U"),
                     (0,0,4,1,"N","U"),
                     (0,0,4,4,"N","D"),
                     (0,3,4,1,"F","D"),
                     (3,0,1,4,"N","D"),
                     (3,3,1,1,"F","D")]
    
    num_filas, num_cols = tablero.shape
    
    for index_f,index_c in index_list: 
        for fiv,civ,ffv,cfv,ori,mode in lista_valores:
        
            f_inicio = np.clip(index_f-fiv,0, num_filas)
            c_inicio = np.clip(index_c-civ,0, num_cols)
            
            f_final = np.clip(index_f+ffv,0, num_filas)
            c_final = np.clip(index_c+cfv,0, num_cols)
            
            ventana = tablero[f_inicio:f_final, 
                            c_inicio:c_final]
            
            
            diagonal = np.diag(ventana)
            if mode == "D":
               
                if ori == "F":
                    diagonal = np.diag(np.fliplr(ventana))
                    
                if np.all(diagonal == 1) and np.size(diagonal) == 4:
                    return True
            
                if np.all(diagonal == 2) and np.size(diagonal) == 4:
                    return True
            
            if mode == "U":
               
                if np.all(ventana == 2) and np.size(ventana) == 4:
                    return True
                
                if np.all(ventana == 1) and np.size(ventana) == 4:
                    return True
                          
    
    

            

            
def admin_fichas(tablero):
    lista_index = encontrar_fichas(tablero)
    if not lista_index:
        return False
    
    if encontrar_4(tablero,lista_index):
        return True
    
continua = tk.BooleanVar(value=True)
def end():
    global continua
    continua.set(False)     



boton_end = tk.Button(
            conecta_4,
            text="terminar",
            bg="#496f70",
            font=fuente,
            command = end
        )

boton_end.pack(
    expand=True,
    fill="both"
)  

  
def juego(tablero):
    global columna

    puntaje_j = {"jugador_1":0,
                 "jugador_2":0}


    while True:

        nf,nc = tablero.shape
        tablero = np.zeros((nf,nc),dtype=int,order="C") 
        alternar = True
        display.config(text= tablero)
        while not admin_fichas(tablero):
            

            conecta_4.wait_variable(columna)
 
            if alternar:
                p = 1
            else:
                p = 2
            
            for i,c in enumerate(tablero[:,columna.get()][::-1]):
                    
                if c == 0:
                        
                    tablero[:,columna.get()][::-1][i] = p
                    alternar = not alternar     
                    break
            display.config(text= tablero)
            columna.set(9)

        

        if p == 1:
            puntaje_j["jugador_1"] += 1 
        else:
            puntaje_j["jugador_2"] += 1    
            
        if not continua.get():
            
            if puntaje_j["jugador_1"] > puntaje_j["jugador_2"]:
                ganador = list(puntaje_j.keys())[0]
            elif puntaje_j["jugador_1"] < puntaje_j["jugador_2"]:
                ganador = list(puntaje_j.keys())[1]
            else:
                print("empate")
                break
            
            print(f"{ganador} a ganado, puntaje: {puntaje_j[ganador]}",)
            break
            
    
            

juego(estructura_vacia)
