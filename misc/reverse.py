def reverse(x):
    #reverse = []
    # length = len(x)
    reverse = x[::-1]
    return reverse
print reverse([1,2,3,4])
print reverse(reverse([1,2,3,4]))

def reverse2(x):
    reverse = []
    length = len(x)
    while length >=0:
        reverse.append(x[length-1])
        length = length - 1
    return reverse
print reverse2([1,2,3,4])
print reverse2(reverse2([1,2,3,4]))
