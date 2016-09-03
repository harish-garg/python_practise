def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    print(result)

factorial(1)
factorial(3)
factorial(5)
