import random

print('-'*50)
print ('          Guess that number game')
print('-'*50)
print()

the_number = random.randint(0, 100)
guess = -1
name = input('What is your name?\n')
while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('sorry {1}, your guess of {0} is too low'.format(guess, name))
    elif guess > the_number:
        print('sorry {1}, your guess of {0} is too high'.format(guess, name))
    else:
        print('good job {1}, {0} was right'.format(guess, name))
print('Done')