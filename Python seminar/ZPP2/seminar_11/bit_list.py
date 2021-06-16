# bit je číslo 0 nebo 1.

# bit_not, bit_and, bit_or, bit_xor

def bit_not(bit):
	"""Negace bitu"""
	if not bit:
		return 1
	else:
		return 0
#print(bit_not(0)) # 1
#print(bit_not(1)) # 0


def bit_and(f_bit, s_bit):
	"""Logická konjukce"""
	if f_bit and s_bit:
		return 1
	else:
		return 0
#print(bit_and(1, 1)) # 1


def bit_or(f_bit, s_bit):
	"""Logická disjunkce"""
	if f_bit or s_bit:
		return 1
	else:
		return 0
#print(bit_or(0, 1)) # 1


def bit_xor(f_bit, s_bit):
	"""Exkluzivní disjunkce"""
	if (f_bit and s_bit) or (not f_bit and not s_bit):
		return 0
	else:
		return 1


"""
print(bit_xor(0, 0)) # 0
print(bit_xor(0, 1)) # 1
print(bit_xor(1, 0)) # 1
print(bit_xor(1, 1)) # 0
"""

# Pomocné funkce.


def list_map(function, lst):
    """Vrátí seznam výsledků aplikací funkce na prvky seznamu."""
    result = []
    for element in lst:
        new_element = function(element)
        result += [new_element]
    return result


"""
list_map(lambda n: n ** 2, [1, 2, 3])
"""


def list_zip(list1, list2):
    """"Vrátí seznam dvojic, kde každá dvojice je tvořena prvkem prvního seznamu a pozičně odpovídajícímu prvku druhého seznamu."""
    result = []
    for i in range(len(list1)):
        result += [[list1[i], list2[i]]]
    return result


"""
list_zip([1, 2, 3], [4, 5, 6])
"""


def two_list_map(function, list1, list2):
    """Vrátí seznam výsledků aplikací funkce na každý prvek seznamu list1 a pozičně odpovídající prvek seznamu list2."""
    return list_map(lambda pair: function(pair[0], pair[1]), list_zip(list1, list2))


"""
two_list_map(lambda n,m: n + m, [1, 2, 3], [4, 5, 6])
"""
# bit_list je seznam bitů.


def bit_list_not(blist):
	"""Bitová negace seznamu bitů"""
	return list_map(bit_not, blist)
#print(bit_list_not([0, 1, 0, 1])) # [1, 0, 1, 0]


def bit_list_and(blist1, blist2):
	"""Bitová konjukce seznamu bitů"""
	return two_list_map(bit_and, blist1, blist2)
#print(bit_list_and([0, 0, 1, 1], [0, 1, 0, 1])) # # [0, 0, 0, 1]


def bit_list_or(blist1, blist2):
	"""Bitová disjunkce seznamu bitů"""
	return two_list_map(bit_or, blist1, blist2)
#print(bit_list_or([0, 0, 1, 1], [0, 1, 0, 1])) # [0, 1, 1, 1]


def bit_list_xor(blist1, blist2):
	"""Bitová exkluzivní disjunkce seznamu bitů"""
	return two_list_map(bit_xor, blist1, blist2)
#print(bit_list_xor([0, 0, 1, 1], [0, 1, 0, 1])) # [0, 1, 1, 0]


def bit_list_left_shift(bit_list, n):
    """Posune seznam bitů o n bitů doleva."""
    if n == 0:
        return bit_list
    else:
        return bit_list_left_shift(bit_list + [0], n - 1)
#bit_list_left_shift([1, 0, 1], 2) # [1, 0, 1, 0, 0]


def bit_list_right_shift(bit_list, n):
    """Posune seznam bitů o n bitů doprava."""
    if n == 0:
        return bit_list
    else:
        return bit_list_right_shift(bit_list[:-1], n - 1)
#bit_list_right_shift([1, 0, 1], 2) # [1]


def fill_zeros(bit_list, n):
    """Doplní na začátek bitového seznamu n nul."""
    if n == 0:
        return bit_list
    else:
        return fill_zeros([0] + bit_list, n - 1)
#fill_zeros([1, 0, 1], 2) # [0, 0, 1, 0, 1]


def align_size(bit_list, n):
    """Doplní na začátek bitového seznamu nuly tak, aby výsledek měl délku n."""
    return fill_zeros(bit_list, n - len(bit_list))
#align_size([1, 0, 1], 5) # [0, 0, 1, 0, 1]


def set_bit_on(bit_list, i):
    """Nastaví bit na indexu i na jedničku."""
    mask = [1]
    mask = bit_list_left_shift(mask, i)
    mask = align_size(mask, len(bit_list))
    return bit_list_or(bit_list, mask)
#set_bit_on([1, 0, 0, 0, 1], 1) # [1, 0, 0, 1, 1]


def set_bit_off(bit_list, i):
    """Nastaví bit na indexu i na nulu."""
    mask = [1]
    mask = bit_list_left_shift(mask, i)
    mask = align_size(mask, len(bit_list))
    mask = bit_list_not(mask)
    return bit_list_and(bit_list, mask)
#set_bit_off([0, 1, 1, 1, 0], 1) # [0, 1, 1, 0, 0]


def get_bit(bit_list, i):
    """Vrátí bitový seznam, který bude mít na prvním místě i-tý bit bitového seznamu bit_list a jinak nuly."""
    result = bit_list_right_shift(bit_list, i)
    mask = [1]
    mask = align_size(mask, len(result))
    return bit_list_and(result, mask)
#get_bit([1, 0, 1, 0], 1) # [0, 0, 1]

# Reprezentace celého nezáporného čísla.


def unsigned_int_to_bit_list(integer):
    """Převede celé nezáporné číslo na seznam bitů."""
    bit_list = []
    while integer != 0:
        bit = integer % 2
        bit_list = [bit] + bit_list
        integer //= 2
    return bit_list
#unsigned_int_to_bit_list(5) # [1, 0, 1]
#unsigned_int_to_bit_list(6) # [1, 1, 0]


def bit_list_to_unsigned_int(blist):
	"""Převede seznam bitů na celé nezáporné číslo."""
	result = 0
	ex = len(blist) - 1
	for i in blist:
		result += blist[i] * (2 ** ex)
		ex -= 1
	return result
#print(bit_list_to_unsigned_int([0, 1, 1, 1])) # 6
#print(bit_list_to_unsigned_int([1, 0, 1])) # 5
