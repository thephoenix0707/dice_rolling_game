from random import randint

user_input = raw_input('Would you like to roll a dice, enter \'y\' or \'n\': ')

if user_input == 'y':
    user_choice = raw_input('Guess your number: ')
    computer_choice = randint(1, 6)
    print(computer_choice)
    if user_choice == computer_choice:
        print 'You are right, congrats!'
    else:
        print 'Try again.'
elif user_input == 'n':
    print 'You quit.'
else:
    print 'Enter a valid choice.'
