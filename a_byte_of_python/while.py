number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('You got it right.')
        running = False
    elif guess < number:
        print('No, it\'s little higher than that.')
    else:
        print('No, it\'s lower than that.')
else:
    print('The while loop is over.')

print('Done')
