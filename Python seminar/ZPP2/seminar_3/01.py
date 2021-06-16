def list_reduce(function, initial, lst):
    result = initial
    for el in lst:
        result = function(result, el)
    return result


def list_filter(predicate, lst):
    def reduce_function(result, val):
        if predicate(val):
            return result + [val]
        else:
            return result
    return list_reduce(reduce_function, [], lst)


def list_map(function, lst):
    def reduce_function(result, val):
        return result + [function(val)]
    return list_reduce(reduce_function, [], lst)


def square(number):
  return number ** 2


print(list_map(square, [1, 2, 3]))  # [1, 4, 9]


def is_even(number):
  return number % 2 == 0


print(list_filter(is_even, [1, 2, 3]))  # [2]
