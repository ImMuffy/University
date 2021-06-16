#1
vstup = 'Ahoj Jarmilo ty kundo'
slova = vstup.split(' ')
#print(slova)


#2
l1 = [[1, 2, 3], [8, 56, 22]]
l2 = [1, 2, 5]

def is_sublist(l1, l2):
    is_suplist = False

    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i][j] != l2[j]:
                is_suplist = False
                break
            is_suplist = True
        if is_suplist:
            return True

    return is_suplist

#print(is_sublist(l1, l2))


#3
matice = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]

def matice_prohoz(matice):
    listm = [[], [], []]
    radky = len(matice)
    sloupce = max(map(len, matice))
    k = 0

    for i in range(sloupce):
        print_row(matice, radky, k)       
        k += 1
        
def print_row(matice, radky, k):
    radek = []
    for i in range(radky):
        radek.append(matice[i][k])
    print(radek)

#matice_prohoz(matice)


#4
n = 8

def jednotkova_matice(n):
    radky = sloupce = n
    jednicka = 0

    for i in range(radky):
        row(sloupce, jednicka)
        jednicka += 1


def row(sloupce, jednicka):
    l = []
    for i in range(sloupce):
        if i != jednicka: 
            l.append(0)
        else:
            l.append(1)
    print(l)

#jednotkova_matice(n)


#5
def list_zbytky(l, n):
    mylist = []
    j = 0

    while j != n:
        sub = []

        for i in range(len(l)):
            if l[i] % n == j:
                sub.append(l[i])
        
        mylist.append(sub)
        j += 1
    
    print(mylist)

#list_zbytky([1, 2, 3, 3, 8, 5, 4], 3)


#6
def dama_sachovnice():
    pole = 8
    sachovnice = []
    sude = True
    bile = 1
    cerne = 2
    prazdno = 0
    
    #černí: 0 - 2
    for i in range(3):
        radek = [prazdno] * pole
        for j in range(pole):
            if not sude and j % 2 == 0:
                radek[j] = cerne
            elif sude and j % 2 == 1:
                radek[j] = cerne
        
        sachovnice.append(radek)
        sude = not sude
        
    #prázdno 3 - 4
    sachovnice.append([prazdno] * pole)
    sachovnice.append([prazdno] * pole)
    sude = True
    
    #bílí 5 - 7
    for i in range(3):
        radek = [prazdno] * pole
        for j in range(pole):
            if sude and j % 2 == 0:
                radek[j] = bile
            elif not sude and j % 2 == 1:
                radek[j] = bile

        sachovnice.append(radek)
        sude = not sude

    radky = max(map(len, sachovnice))
    k = 0

    for i in range(radky):
        print_radek(sachovnice, pole, k)
        k += 1
    
def print_radek(list, radky, k):
    radek = []
    for i in range(radky):
        radek.append(list[k][i])
    print(radek)

#dama_sachovnice()

