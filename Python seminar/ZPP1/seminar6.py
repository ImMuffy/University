#1
fahr = 81
celsius = 5 * (fahr - 32) / 9
print(celsius)

#2
celsius = 27.2
fahr = (celsius * 9 / 5) + 32
print(fahr)

#3
# n = (n - 1) + (n - 2)
fib = 7
n = 0
n1 = 0
n2 = 1
count = 0

while count < fib:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    count += 1

#6
n = 6
citatel = 1
soucet = 0

for i in range(1, n + 1):
    soucet += citatel / i

print(soucet)
