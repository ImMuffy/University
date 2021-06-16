#1
n = 123
n1 = n
result = 0

while n1 > 0:
    digit = n1 % 10  
    n1 //= 10        
    result += digit  

print(result)

#5 se stringem
slovo = "oko"
is_palindrom = True
j = len(slovo) - 1

for i in range(len(slovo)):
    if slovo[i] != slovo[j]:
        is_palindrom = False
    j -= 1

print(is_palindrom)

#10
n = 80
k = 40
nejmensi = n

for i in range(1, n + 1):
    if n % i == 0 and i >= k and i < nejmensi:
        nejmensi = i
        break

print(nejmensi)


### Pro Toma
n = 123
n1 = n
result = 0

digit = n1 % 10  # poslední cifra
n1 //= 10        # dělení na celá čísla
