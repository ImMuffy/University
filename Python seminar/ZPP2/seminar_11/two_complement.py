'''
import bit_list as bl  # přesně definovat cestu

def number_to_bit_list(number, size):
	"""Převede celé číslo na seznam bitů podle dvojkového doplňkového kódu."""
    if number >= 0:
        bit_list = bl.unsigned_int_to_bit_list(number)
        if size <= len(bit_list):
            raise ValueError('Size of bit list is to small.')
        return bl.align_size(bit_list, size)
    else:
        return bl.bit_list_not(number_to_bit_list(-number-1, size))



print(number_to_bit_list(-124, 8)) # [1, 0, 0, 0, 0, 1, 0, 0]
print(number_to_bit_list(-3, 3)) # [1, 0, 1]
print(number_to_bit_list(3, 3)) # [0, 1, 1]



def bit_list_to_number(bit_list):
    """Převede seznam bitů na celé číslo podle dvojkového doplňkového kódu."""
    sign_bit = bit_list[0]
    if sign_bit == 0:
        return bl.bit_list_to_unsigned_int(bit_list)
    else:
        return -bit_list_to_number(bl.bit_list_not(bit_list))-1



bit_list_to_number(bit_list)

bit_list_to_number([0, 1, 1]) # 3
bit_list_to_number([1, 0, 1]) # -3

bit_list_to_number(number_to_bit_list(-124, 8))
'''
