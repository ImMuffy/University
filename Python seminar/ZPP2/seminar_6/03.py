# Fronta pomocí spojového seznamu

# Prázdný spojový seznam je pouze hodnota EMPTY.
EMPTY = []

# Neprázdný spojový seznam určuje první prvek a zbytek. Zbytek je opět spojový seznam.


def cons(value, lilist):
    """Vytvoří nový spojový seznam, kde první prek bude value a zbytek lilist."""
    return [value, lilist]


def get_first(lilist):
    """Vrátí první prvek neprázdného spojového seznamu."""
    return lilist[0]


def get_rest(lilist):
    """Vrátí zbytek neprázdného spojového seznamu."""
    return lilist[1]


def set_first(lilist, value):
    """Nastaví první prvek spojového seznamu."""
    lilist[0] = value


def set_rest(lilist, rest_ll):
    """Nastaví zbytek spojového seznamu."""
    lilist[1] = rest_ll


def is_empty(lilist):
    """Rozhodne, zda je spojový seznam prázdný."""
    return lilist == EMPTY

# Implementujte frontu pomocí zapouzdřeného spojového seznamu.
# - make_queue
# - is_queue_empty
# - enqueue
# - dequeue


def make_queue():
    """Vytvoří frontu."""
    return [EMPTY, EMPTY]


def get_front(queue):
    """Vrátí spojový seznam prvků fronty."""
    return queue[0]


def set_front(queue, front):
    """Nastaví spojový seznam prvků."""
    queue[0] = front


def get_back(queue):
    """Vrátí spojový seznam obsahující pouze poslední prvek fronty."""
    return queue[1]


def set_back(queue, back):
    """Nastaví spojový seznam s posledním prvkem fronty."""
    queue[1] = back


def is_queue_empty(queue):
    """Rozhodne, zda je fronta prázdná."""
    return is_empty(get_front(queue))


def enqueue(value, queue):
    """Přidá hodnotu na konec fronty."""
    tail = cons(value, EMPTY)
    if is_queue_empty(queue):
        set_front(queue, tail)
        set_back(queue, tail)
    else:
        back = get_back(queue)
        set_rest(back, tail)
        set_back(queue, tail)


q = make_queue()
print(q)
enqueue(1, q)
print(q)
enqueue(2, q)
print(q)


def dequeue(queue):
    """Odebere hodnotu ze začátku fronty a vrátí ji."""
    ll1 = get_front(queue)
    ll2 = get_rest(ll1)
    set_front(queue, ll2)
    if is_empty(ll2):
        set_back(queue, EMPTY)
    return get_first(ll1)


print(dequeue(q))
print(q)
print(dequeue(q))
print(q)
