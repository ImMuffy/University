def list_reduce(function, initial, lst):
    result = initial
    for el in lst:
        result = function(result, el)
    return result


def list_filter(predicate, lst):
    return list_reduce(
        lambda result, val: result + [val] if predicate(val) else result,
        [],
        lst)


def list_map(function, lst):
    return list_reduce(
        lambda result, val: result + [function(val)],
        [],
        lst)


print(list_map(
    lambda number: number ** 2,
    [1, 2, 3]))  # [1, 4, 9]

print(list_filter(
    lambda number: number % 2 == 0,
    [1, 2, 3]))  # [2]
