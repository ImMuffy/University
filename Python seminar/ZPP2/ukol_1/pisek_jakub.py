# Prázdný spojový seznam
EMPTY = []

def cons(value, lilist):
	"""Vytvoří nový spojový seznam, kde první prek bude value a zbytek lilist."""
	return [value, lilist]

def is_empty(lilist):
	"""Rozhodne, zda je spojový seznam prázdný."""
	return lilist == EMPTY

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

def is_multiple(value, multiple):
	"""Rozhodne, zda je číslo prvního argumentu násobek čísla druhého argumentu"""
	if value % multiple == 0:
		return True
	else:
		return False


# První verze - nesmí změnit LL

def delete_multiple_ll1(multiple, lilist):
	"""Odstraní ze spojového seznamnu všechny násobky čísla"""
	if is_empty(lilist):
		return EMPTY
	else:
		if is_multiple(get_first(lilist), multiple):
			return delete_multiple_ll1(multiple, get_rest(lilist))
		else:
			first_element = get_first(lilist)
			return cons(first_element, delete_multiple_ll1(multiple, get_rest(lilist)))

ll1 = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6, cons(7, cons(8, cons(9, cons(10, EMPTY))))))))))
ll2 = cons(1, cons(2, cons(3, cons(4, cons(5, cons(4, cons(6, cons(7, cons(8, cons(9, EMPTY))))))))))
ll1 = cons(2, cons(1, cons(4, EMPTY)))
ll2 = cons(2, cons(1, cons(3, EMPTY)))

print("První verze:")
print(ll1)
print(delete_multiple_ll1(2, ll1))
print(ll1)
print(ll2)
print(delete_multiple_ll1(2, ll2))
print(ll2)


# Druhá verze - může změnit LL

def delete_multiple_ll2(multiple, lilist):
	"""Odstraní ze spojového seznamnu všechny násobky čísla"""
	if is_empty(lilist):
		return EMPTY
	else:
		if is_multiple(get_first(lilist), multiple):
			return delete_multiple_ll2(multiple, get_rest(lilist))
		else:
			rest_result = delete_multiple_ll2(multiple, get_rest(lilist))
			set_rest(lilist, rest_result)
			return lilist


ll1 = cons(2, cons(1, cons(4, EMPTY)))
ll2 = cons(1, cons(2, cons(4, cons(3, EMPTY))))

print("\nDruhá verze:")
print(ll1)
ll1 = delete_multiple_ll2(2, ll1)
print(ll1)
print(ll2)
ll2 = delete_multiple_ll2(2, ll2)
print(ll2)

