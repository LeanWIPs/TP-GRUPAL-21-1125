items = []   # lista de números
n = 0        # tamaño
# variables del algoritmo
i = j = None


def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 1   


def step():
    

    global items, n, i, j
    # finalización
    if i >= n - 1:
        return {"a": -1, "b": -1, "swap": False, "done": True}

    # comparar items[i] con items[j]
    if items[i] > items[j]:
        # swap real
        items[i], items[j] = items[j], items[i]
        resultado = {"a": i, "b": j, "swap": True, "done": False}
    else:
        resultado = {"a": i, "b": j, "swap": False, "done": False}

    # avanza punteros 
    j += 1
    if j >= n:
        i += 1
        j = i + 1

    return resultado