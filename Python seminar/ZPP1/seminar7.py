#1
def fib_list(fib):
    n = 0
    n1 = 0
    n2 = 1
    count = 0
    flist = []

    while count < fib:
        flist.append(n1)
        n = n1 + n2
        n1 = n2
        n2 = n
        count += 1
    
    return flist
#print(fib_list(7))

#2
def fib_list_n(n):
    n1 = 0
    n2 = 1
    count = 2
    flist = [n1, n2]

    while count < n:
        flist.append(flist[count - 1] + flist[count - 2])
        count += 1

    return flist
#print(fib_list_n(12))

#3
def produkt_list(lis):
    if lis == []:
        return []
    else:
        result = 1
        for l in lis:
            result *= l
        return result
#print(produkt_list([]))

#4
def reverse(mylist):
    hlist = []

    for i in range(len(mylist) - 1, -1, -1):
        hlist.append(mylist[i])
    
    return hlist
#print(reverse([1, 2, 3, 8, 0]))

#5
def sublist(mylist, spodni, horni):
    if spodni > horni: return
    slist = []

    for i in range(spodni, horni):
        slist.append(mylist[i])

    return slist
#print(sublist([5, 4, 3, 2, 1], 0, 3))

#6
def eqlist(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
    
    return True
#print(eqlist([1, 3, 4],[1, 3, 4]))    