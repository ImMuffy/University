# list_zip

# list_zip([1, 2, 3], [4, 5, 6]) # [[1, 4], [2, 5], [3, 6]]

def list_zip(list1, list2):
  result = []
  for i in range(len(list1)):
    el1 = list1[i]
    el2 = list2[i]
    result += [[el1, el2]]
  return result


def list_reduce(function, initial, lst):
    result = initial
    for el in lst:
        result = function(result, el)
    return result


def list_map(function, lst):
    def reduce_function(result, val):
        return result + [function(val)]
    return list_reduce(reduce_function, [], lst)


def lists_add(list1, list2):
  return list_map(
      lambda pair: pair[0] + pair[1],
      list_zip(list1, list2))

# lists_add([1, 2, 3], [4, 5, 6]) # [5, 7, 9]

def lists_power(bases, exps):
  return list_map(
      lambda pair: pair[0] ** pair[1],
      list_zip(bases, exps))
