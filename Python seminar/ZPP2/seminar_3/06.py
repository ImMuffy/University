def add(num1, num2):
    return num1 + num2


def create_add_constant(constant):
    return lambda num: add(constant, num)


add_two = create_add_constant(2)


def curry2(function, arg1):
  return lambda arg2: function(arg1, arg2)


add_two2 = curry2(add, 2)
