def product(list):
    product = 1
    for item in list:
        product = product * item
    return product

def factorial(x):
    factorial = 1
    if x == 0:
        factorial = x
    else:
        list = range(x+1)[1:]
        factorial = product(list)
    return factorial

print factorial(0)
print factorial(1)
print factorial(2)
print factorial(3)
print factorial(4)
