number = 23
guess = int(input("Enter and Integer : "))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you did not win any prizes.)')

elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block...
else:
    print('No, it is a lower than that')
    # you must have gussed > number to reach here.

print('Done')
# This last statment is always executed.
# afer the if statment if executed.
