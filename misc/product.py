def product(list):
    product = 1
    for item in list:
        product = product * item
    return product

print product([1,2,3])
print product([])
print product([0])
print product([0, 1])
print product([1])

