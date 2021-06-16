n = "Python"
reverse = ""

for i in range(len(n) - 1, -1, -1):
    reverse += n[i]

print(reverse)

#1
t = "456"
num = int(t)
print(type(num))

#2
num = 123
t = str(num)
print(type(t))
