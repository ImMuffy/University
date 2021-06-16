def list_reduce(function, initial, lst):
    result = initial
    for el in lst:
        result = function(result, el)
    return result


def are_every(predicate, lst):
  return list_reduce(
      lambda result, el: False if not result else predicate(el),
      True,
      lst)

# are_every(predicate, lst)

# are_every(lambda num: num % 2 == 0, [2, 4, 6]) # True
# are_every(lambda num: num % 2 == 0, [2, 5, 4, 6]) # False
# are_every(lambda num: num % 2 == 0, []) # True


def are_all_less(number, lst):
  return are_every(
      lambda arg: arg < number,
      lst)

# are_all_less(4, [1, 2, 3]) # True
# are_all_less(4, [4, 1, 2, 3]) # False
