# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0 #vueltas que dio
    j = 0 #indice en que esta posicionado

def step():
    #cuando termina o ya esta ordenada cuando la lista tiene 0 o 1 elemento.
    global items, n,i,j # global: "Voy a usar y modificar variables que están definidas FUERA de la función"
    if n<=1:
        return{"done":True}
    
    #comparamos items
    
    if items[j]>items[j+1]: #compara la posicion en la que esta con la siguiente
        items[j],items[j+1]=items[j+1],items[j] #cambio de posicion item j cambia por item j+1
        resultado={"a": j, "b": j+1, "swap": True, "done": False} #swap el que el intercambio ya se hizo
    else:
        resultado={"a": j, "b": j+1, "swap": False, "done": False}
    j+=1# para que avance al siguiente indice
    if(j+1 == n-i-0): #j+1 == n-i-2 habia puesto asi pero los ultimos 2 no se ordenaban
        j=0      
        i+=1 
    if(i==n-1):
        resultado={"done": True}
    return resultado

#askdaklsda<zx<zx<
