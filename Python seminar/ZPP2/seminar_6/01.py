# Zapouzdřený spojový seznam

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

# Odstranění prvku na indexu


def delete_second(lilist):
    third_rest = get_rest(get_rest(lilist))
    set_rest(lilist, third_rest)


"""
ll1 = cons(1, cons(2, cons(3, EMPTY)))
print(ll1)
delete_second(ll1)
print(ll1) # [1, [3, []]]
"""


def delete_nth(lilist, n):
    """Odstraní ze spojového seznamu prvek na indexu n. Může změnit spojový seznam."""
    if n == 0:
        return get_rest(lilist)
    else:
        current = lilist
        for i in range(n - 1):
            current = get_rest(current)
        delete_second(current)
        return lilist


"""
ll1 = cons(1, cons(2, cons(3, cons(4, EMPTY))))
print(ll1) # [1, [2, [3, [4, []]]]]
ll1 = delete_nth(ll1, 2)
print(ll1) # [1, [2, [4, []]]]
ll1 = delete_nth(ll1, 1)
print(ll1) # [1, [4, []]]
ll1 = delete_nth(ll1, 1)
print(ll1) # [1, []]
ll1 = delete_nth(ll1, 0)
print(ll1) # []
"""

# Zapouzdřený spojový seznam elilist - (encapsulation linked list)


def make_elilist(lilist):
    """Zapouzdří spojový seznam."""
    return [lilist]


def get_lilist(elilist):
    """Vrátí zapouzdřený seznam."""
    return elilist[0]


def set_lilist(elilist, lilist):
    """Nastaví spojový seznam zapouzdření."""
    elilist[0] = lilist


def e_delete_first(elilist):
    """Odstraní první prvek seznamu."""
    set_lilist(elilist, get_rest(get_lilist(elilist)))


"""
ll1 = cons(1, cons(2, EMPTY))
e1 = make_elilist(ll1)
print(e1)
e_delete_first(e1)
print(e1)
"""

# Napište funkci, která odstraní ze zapouzdřeného spojového seznamu prvek na indexu n. Funkce nesmí nic vracet. Může změnit zapouzdřený seznam.


def e_delete_nth(ell, n):
	"""Odstraní prvek ze zapouzdřeného seznamu na indexu n. Může zapouzdřený seznam změnit."""
	ll1 = get_lilist(ell)
	ll2 = delete_nth(ll1, n)
	set_lilist(ell, ll2)


ll1 = cons(1, cons(2, cons(3, cons(4, EMPTY))))
ell1 = make_elilist(ll1)
e_delete_nth(ell1, 2)
print(ell1)  # [[1, [2, [4, []]]]]
