EMPTY = []

# lilist ... linked list


def cons(val, lilist):
    return [val, lilist]


ll1 = cons(1, cons(2, cons(3, EMPTY)))


def get_first(lilist):
    return lilist[0]


def get_rest(lilist):
    return lilist[1]


def is_empty(lilist):
    return lilist == EMPTY

# 1. get_second(lilist)


def get_second(lilist):
	return get_first(get_rest(ll1))

#print(get_second(ll1)) #  2


# 2. get_third(lilist)
def get_third(lilist):
	return get_first(get_rest(get_rest(ll1)))

#print(get_third(ll1)) #  3


# 3. nth(lilist, n)
# n = 0 .. první prvek

def nth_rest(lilist, n):
    for i in range(n):
        lilist = get_rest(lilist)
    return lilist

#print(nth_rest(ll1, 1))


def nth(lilist, n):
    lilist = nth_rest(lilist, n)
    return get_first(lilist)

#print(nth(ll1, 2)) # 3


# 4. length(lilist)
def length(lilist):
	n = 0
	while not is_empty(lilist):
		lilist = get_rest(lilist)
		n += 1
	return n

#print(length(ll1)) # 3


# 5.* length_rec(lilist)
def length_rec(lilist):
	if is_empty(lilist):
		return 0
	else:
		return 1 + length_rec(get_rest(lilist))

#print(length_rec(ll1)) # 3


# 6. lilist_range(n)
def lilist_range(n):
    lilist = EMPTY
    for i in range(n):
        lilist = cons(n - i - 1, lilist)
    return lilist

#print(lilist_range(3)) # [0, [1, [2, []]]]


# 7. reverse(lilist)
def reverse(lilist):
    result = EMPTY
    while not is_empty(lilist):
        first = get_first(lilist)
        result = cons(first, result)
        lilist = get_rest(lilist)
    return result

#print(reverse(ll1)) # [3, [2, [1, []]]]


# 8. is_member(val, lilist)
def is_member(val, lilist):
	while not is_empty(lilist):
		if get_first(lilist) == val:
			return True
		else:
			lilist = get_rest(lilist)
	return False

#print(is_member(1, ll1)) # True
#print(is_member(4, ll1)) # False


# 9. is_member_rec(val, lilist)
#  - jako is_member, ale rekurzivní
def is_member_rec(val, lilist):
	if is_empty(lilist):
		return False
	elif get_first(lilist) == val:
		return True
	else:
		return is_member_rec(val, get_rest(lilist))

#print(is_member_rec(1, ll1)) # True
#print(is_member_rec(4, ll1)) # False


# 10. append(lilist1, lilist2)
def append(ll1, ll2):
	if is_empty(ll1):
		return ll2
	elif is_empty(ll2):
		return ll1

	ll1 = reverse(ll1)
	while not is_empty(ll1):
		ll2 = cons(get_first(ll1), ll2)
		ll1 = get_rest(ll1)

	return ll2


ll2 = cons(4, cons(5, cons(6, EMPTY)))

#print(append(ll1, ll2)) # [1, [2, [3, [4, [5, [6, []]]]]]]


# 11. * lilist_map(function, lilist)

# print(lilist_map(lambda i: i + 1, ll1 )) # [2, [3, [4, []]]]

# 12. * lilist_filter(predicate, lilist)

# print(lilist_filter(lambda i: i % 2 == 0, ll1)) # [2, []]

# 13. * lilist_reduce(function, initial, lilist)

# print(lilist_reduce(lambda a, b: a + b, 0, ll1)) # 6

# 14. * Napsat lilist_map a lilist_filter pomocí lilist_reduce.


# 15. is_sorted(lilist)
def is_sorted(ll):
	while not is_empty(ll):
		if get_first(ll) > get_first(get_rest(ll1)):
			return True
		ll = get_rest(ll)
	return False


print(is_sorted(ll1))  # True
print(is_sorted(cons(2, cons(1, EMPTY))))  # False

# 16. is_member_in_sorted(val, lilist)

# 17. add_to_sorted(val, lilist)

# l3 = EMPTY
# l3 = add_to_sorted(5, l3)
# l3 = add_to_sorted(8, l3)
# l3 = add_to_sorted(1, l3)
# l3 = add_to_sorted(6, l3)
# print(l3) # [1, [5, [6, [8, []]]]]
