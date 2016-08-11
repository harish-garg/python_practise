# Get the no. of tests from the CLI
no_of_tests = int(input())

# get the tests and add them to a list
test_strings = []
for n in range(no_of_tests):
    str = input()
    test_strings.append(str)

# Process the test strings
for t in test_strings:
    length = len(t)
    index = 0
    odd_str = ""
    even_str = ""
    while index < length:
        if (index % 2) == 0:
            even_str += t[index]
            index += 1
        else:
            odd_str += t[index]
            index += 1
    print(even_str, odd_str)
