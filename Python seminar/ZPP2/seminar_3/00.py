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


def list_zip(list1, list2):
    result = []
    for i in range(len(list1)):
        result += [[list1[i], list2[i]]]
    return result


def is_multiple(n, m):
    return n % m == 0


def curry2(function, arg1):
    return lambda arg2: function(arg1, arg2)

# 1. are_all_div_by
# použijete: are_every a is_multiple


def are_all_div_by(num, lst):
	return are_every(
		lambda arg: is_multiple(arg, num),
		lst)

#print(are_all_div_by(2, [2, 4, 8, 6])) # True


# 2. are_all_even
# použít: are_all_div_by a curry2
are_all_even = curry2(are_all_div_by, 2)

#print(are_all_even([2, 4, 6])) # True


# 3. are_all_pairs_div
# použít: curry2 a are_every
are_all_pairs_div = curry2(
	are_every,
	lambda pair: is_multiple(pair[0], pair[1])
)

#print(are_all_pairs_div([[4, 2], [6, 3], [7, 1]])) # True

# 4. are_all_div
# použít: are_all_pairs_div a list_zip

# are_all_div([4, 6, 7], [2, 3, 1]) # True
