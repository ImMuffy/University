#import bit_list as bl
#import two_complement as tc
from math import floor

# bitový součin (AND)
print(3 & 5)
"""
bl1 = number_to_bit_list(3, 4)
bl2 = number_to_bit_list(5, 4)
result_bl = bit_list_and(bl1, bl2)
result = bit_list_to_number(result_bl)
"""

# bitový součet (OR)
print(3 | 5)

"""
bl1 = number_to_bit_list(3, 4)
bl2 = number_to_bit_list(5, 4)
result_bl = bit_list_or(bl1, bl2)
result = bit_list_to_number(result_bl)
"""

# bitový exklusivní součet (XOR)
print(3 ^ 5)

"""
bl1 = number_to_bit_list(3, 4)
bl2 = number_to_bit_list(5, 4)
result_bl = bit_list_xor(bl1, bl2)
result = bit_list_to_number(result_bl)
"""

# bitová negace (NOT)
print(~1)
"""
bl = number_to_bit_list(1, 8)
result_bl = bit_list_not(bl)
bit_list_to_number(result_bl)
"""

print(~0)

# Záporná čísla
print(5 & -2)
"""
number_to_bit_list(5, 8)
number_to_bit_list(-2, 8)
"""

# bitový posun vlevo
print(4 << 1)
"""
number_to_bit_list(4, 8)
number_to_bit_list(8, 8)
"""
print(-4 << 1)
"""
number_to_bit_list(-4, 8)
it_list_to_number([1, 1, 1, 1, 1, 1, 0, 0,0])
"""

# bitový posun vpravo
print(4 >> 1)
print(-4 >> 1)
print(-1 >> 1)

# Úkoly:


def set_bit_on(n, i):
    """Nastaví i-tý bit na jedničku."""
    pass


"""
set_bit_on(4, 0) # 5
set_bit_on(4, 3) # 12
"""


def set_bit_off(n, i):
    """Nastaví i-tý bit na nulu."""
    pass


"""
set_bit_off(8, 3) # 0
set_bit_off(-1, 2) # -5
"""


def get_bit(n, i):
    """Vrátí i-tý bit."""
    pass


"""
get_bit(8, 3) # 1
get_bit(8, 2) # 0
get_bit(-1, 2) # 1
get_bit(-1, 10000) # 1
"""

# Datum je pár [den, měsíc], kde den je číslo dne a měsíc je číslo měsíce. Například [26, 4] je 26. dubna.


def encode_date(date):
    """Převede datum na bity."""
    pass


"""
encode_date([26, 4]) # vrátí celé číslo
"""


def decode_date(bits):
    """Vrátí datum uložené v bitech."""
    pass


"""
x = # celé číslo reprezentující [26, 4]
encode_date(x) # [26, 4]
"""
