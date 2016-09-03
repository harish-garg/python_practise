n = int(input())
phoneBook = {}
for i in range(n):
    l = input().split(' ')
    phoneBook[l[0]] = l[1]

query = True
while query:
    name = input()
    if name == '':
        break
    elif name in phoneBook:
        print(name + '=' + phoneBook[name])
    else:
        print("Not found")
