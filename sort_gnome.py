
# Gnome Sort — implementación que realiza el swap dentro de step()
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 1   # puntero del gnome (convención clásica)

def init(vals):
    global items, n, i
    items = list(vals)
    n = len(items)
    i = 1

def step():
    global items, n, i

    # casos cortos
    if n <= 1 or i >= n:
        return {"done": True}

    a = i - 1
    b = i

    # si están en orden, avanzamos
    if items[a] <= items[b]:
        i += 1
        return {"a": a, "b": b, "swap": False, "done": False}

    # si están desordenados, hacemos el swap aquí
    items[a], items[b] = items[b], items[a]

    # después del swap, retrocedemos si podemos
    if i > 1:
        i -= 1
    else:
        i += 1

    return {"a": a, "b": b, "swap": True, "done": False}
