# Higher order functions

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value, f):
    return f(first_value + second_value)

print(sum_two_values_and_one(5,2,sum_one))
print(sum_two_values_and_one(5,2,sum_five))

# Closures

def sum_tem(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_clossure = sum_tem(1)

print(add_clossure(5))

# Built-in Higher Order functions

numbers = [2, 5 , 10, 21, 3, 30]

def multiply_two(number):
    return number * 2
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

#Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce

def sum_two_values(first_value, second_value   ):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))

