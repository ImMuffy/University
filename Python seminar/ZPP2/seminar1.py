def list_map(function, lst):
  result = []
  for el in lst:
    new_el = function(el)
    result += [new_el]
  return result

def list_filter(predicate, lst):
	result = []
	for el in lst:
		if predicate(el):
			result += [el]
	return result

# 1.
def map_abs(lst):
	return list_map(abs, lst)

#print(map_abs([-1, 2, -5]))  # [1, 2, 5]


# 2.
def map_len(lst):
	return list_map(len, lst)

#print(map_len([[1, 2], [], [3]]))  # [2, 0, 1]


# 3.
def successor(num):
  return num + 1

def map_row_successor(lst):
  return list_map(successor, lst)

def map_matrix_suc(matrix):
  return list_map(map_row_successor, matrix)

#print(map_matrix_suc([[1, 2], [0, 1]]))  # [[2, 3], [1, 2]]


# 4.
def nonempty(lst):
  return lst

def filter_nonempty(lst):
  return list_filter(nonempty, lst)

#print(filter_nonempty([[], [1, 2], [], [3], [5, 6, 8, 9], ["a"]])) # [[1, 2], [3]]


# 5.
def square(num):
  return num ** 2

def map_square(lst):
  return list_map(square, lst)

def is_positive(num):
  return num > 0

def filter_positive(lst):
  return list_filter(is_positive, lst)

def list_positive_square(lst):
  return map_square(filter_positive(lst))

#print(list_positive_square([1, -2, 3, -3]))  # [1, 9]


# 6. bod je [x, y]
# Funkce převrátí seznam bodů podle x-ové osy.
def point_swap(lst):
  return [lst[0], lst[1] * -1]

def points_x_swap(lst):
  return list_map(point_swap, lst)

#print(points_x_swap([[0, 0], [1, 1], [2, 1]]))  # [[0, 0], [1, -1], [2, -1]]


#7.
def is_even(num):
  return num % 2

def filter_odd(lst):
  return list_filter(is_even, lst)

#print(filter_odd([1, 2, 3, 4, ]))  # [1, 3]


#8.
def start_with_a(word):
  if word and word[0] == 'a':
    return True
  else:
    return False

def filter_start_with_a(lst):
  return list_filter(start_with_a, lst)

#print(filter_start_with_a(['ab', '', 'cd', 'aa'])) # ['ab', 'aa']
