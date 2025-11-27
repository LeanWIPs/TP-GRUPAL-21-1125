# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    global items, n,i,j
    if i>=n:
        {"done": True}
    
    #buscar items 
    if j is None:
        j=i
        return {"a": j, "b": j, "swap": False, "done": False}
    
    if j>0 and items[j-1]>items[j]:
        items[j-1],items[j]=items[j],items[j-1]#swap adyacente= intercambio
        resultado={"a": j-1, "b": j, "swap": True, "done": False}
        j=j-1
        return resultado
    
    #cuando no hay mas que desplazar
    i=i+1
    j=None
    return {"a": i-1, "b": i-1, "swap": False, "done": False}
    
    
   

