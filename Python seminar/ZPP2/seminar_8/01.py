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

# Pomocné funkce

def is_empty(lilist):
    """Rozhodne, zda je spojový seznam prázdný."""
    return lilist == EMPTY

def remove_all_multiples(lilist, n):
    """Odstraní ze spojového seznamu všechna sudá čísla. Seznam lilist nemění."""
    if is_empty(lilist):
        return EMPTY
    else:
        rest_result = remove_all_multiples(get_rest(lilist), n)
        # ...
        return cons(get_first(lilist), rest_result)

def delete_all_multiples(lilist, n):
    """Odstraní ze spojového seznamu všechna sudá čísla. Seznam lilist může změnit."""
    if is_empty(lilist):
        return EMPTY
    else:
        rest_result = remove_all_multiples(get_rest(lilist), n)
        # ...
        set_rest(lilist, rest_result)
        return lilist