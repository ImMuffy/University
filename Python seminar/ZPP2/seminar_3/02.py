def square(number):
  return number ** 2

# lambda p1, ..., pn: e
# p1, ..., pn jsou parametry
# e je výraz


def square2(number): return number ** 2


def add(a, b): return a + b


def add2(a): return lambda b: a + b


def my_abs(num):
  if num < 0:
    return -num
  else:
    return num

# e1 if c else e2

# if c:
#     return e1
# else:
#     return e2


def my_abs2(num): return -num if num < 0 else num
