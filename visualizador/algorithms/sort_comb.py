items = []
n = 0

gap = 0
i = 0
swapped = False

def init(vals):
    global items, n, gap, i, swapped
    items = list(vals)
    n = len(items)
    
    gap = n
    i = 0
    swapped = False


def step():
    global items, n, gap, i, swapped

    # Si ya está todo ordenado
    if gap == 1 and i >= n-1 and not swapped:
        return {"a": -1, "b": -1, "swap": False, "done": True}

    # Si i llegó al final de la pasada
    if i + gap >= n:
        # Reducir gap
        new_gap = int(gap / 1.3)
        gap = max(1, new_gap)

        i = 0
        swapped = False
        return {"a": -1, "b": -1, "swap": False, "done": False}

    # Comparación actual
    a = i
    b = i + gap

    # Realizar comparación y posible swap
    do_swap = False
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        do_swap = True
        swapped = True

    i += 1

    return {"a": a, "b": b, "swap": do_swap, "done": False}
