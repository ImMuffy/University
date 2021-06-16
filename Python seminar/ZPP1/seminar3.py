#1
a = 1
d = 3
n = 5

for i in range(n):
    print(a)
    a = a + d

#2
a = 1
d = 3
n = 5
result = 0

for i in range(n):
    print(i)
    result += a
    a += d
print(result)

#3
x = 15
y = 20

if x > y:
    n = x
else:
    n = y

for i in range(1, n):
    if x % i == 0:
        print("x:", i)
    if y % i == 0:
        print("y:", i)

#9
n = 8
f = 1

if n == 0:
    print(1)
else:    
    for i in range(n):
        if i != 0:
            f = f * (i + 1)

print(f)

#13
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        for j in range(n):
            print("*", end="")
    else:
        for k in range(n):
            if k == 0 or k == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
    print("")

#14
n = 5

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print("")

#15
n = 5
m = 2

#první hvězda
for i in range(n):
    print(" ", end="")
print("*")

for i in range(1, n):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i + m):
        print("*", end="")
    print("")
    m += 1
