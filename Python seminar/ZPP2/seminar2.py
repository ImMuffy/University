# list_reduce
def list_reduce(operation, neutral, lst):
  result = neutral
  for el in lst:
    result = operation(result, el)
  return result


# 1.
def list_add(result, el):
	return result + el

def list_concat(lst):
	return list_reduce(list_add, [], lst)

#print(list_concat([[1, 2], [3, 4], [], [5]]))  # [1, 2, 3, 4, 5]


# 2.
def reverse_operation(result, el):
	return [el] + result

def reverse(lst):
	return list_reduce(reverse_operation, [], lst)

#print(reverse([1, 2, 3, 4]))  # [4, 3, 2, 1]


# 3.
def sum_op(result, el):
	return [result[0] + el[0], result[1] + el[1]]


def bin_sum(lst):
	return list_reduce(sum_op, [0, 0], lst)

#print(bin_sum([[1, 2], [1, 2], [5, 0]]))  # [7, 4]


# 4. *
#list_filter


# compose
def compose(f, g):
  def result_function(val):
    return g(f(val))
  return result_function


def successor(num):
  return num + 1


def square(num):
  return num ** 2


def inverse(num):
  return (-1) * num


# 5.
fourth_power = compose(square, square)
#print(fourth_power(2))  # 16

# 6.
#inverse_of_square(2)  # -4

# 7.
#add_three(2)  # 5

# 8.


def add(n, m):
  return n + m

#f = fix_arg(add, 2) # Vrátí funkci jednoho parametru, která zavolá funkci add s prvním argumentem 2.
#f(3) # 5
