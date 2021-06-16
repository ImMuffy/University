vyraz = '3*7/3'
index = -1
cislo = ''
znamenko = ''

def resicka(vyraz):
    cislo1 = 0
    cislo2 = 0

    #1. a 2. číslo
    cislo1 = next_number(vyraz, index)
    operace = znamenko
    cislo2 = next_number(vyraz, index)
    
    #(1. a 2.) a 3. číslo
    cislo1 = next_operation(cislo1, cislo2, operace)
    cislo2 = next_number(vyraz, index)
    operace = znamenko

    result = next_operation(cislo1, cislo2, operace)

    return result

def next_number(vyraz, x):
    global cislo
    global znamenko
    global index
    cislo = ''

    for i in range(x + 1, len(vyraz)):
        if vyraz[i] != '+' and vyraz[i] != '-' and vyraz[i] != '*' and vyraz[i] != '/':
            cislo += vyraz[i]
        elif vyraz[i] == '+':
            index = i
            znamenko = '+'
            break
        elif vyraz[i] == '-':
            index = i
            znamenko = '-'
            break
        elif vyraz[i] == '*':
            index = i
            znamenko = '*'
            break
        elif vyraz[i] == '/':
            index = i
            znamenko = '/'
            break

    return int(cislo)

def next_operation(cislo1, cislo2, operace):
    return {
        '+':(cislo1 + cislo2),
        '-':(cislo1 - cislo2),
        '*':(cislo1 * cislo2),
        '/':(cislo1 / cislo2),
    }[operace]


print(resicka(vyraz))
