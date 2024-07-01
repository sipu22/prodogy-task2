import random

def guess_the_number():
    number_to_guess=random.randint(1,100)
    attempts=0
    guessed_correctly=True

    print('Welcome to the Number Guessing Game')
    print('I have generated a random number between 1 to 100')
    print('Can you guess it what it is?')

    while guessed_correctly:
        try:
            guess=int(input('Enter your guess:'))
            attempts+=1

            if guess<number_to_guess:
                print('Too Low! Try again')

            elif guess>number_to_guess:
                print('Too High! Try again')

            else:
                guessed_correctly=True
                print(f"Congratulation! You have guessed the number {number_to_guess}")
                print(f'It took you {attempts} attempts')

        except ValueError:
            print('Invalid input.Please enter a valid integer')

if __name__ == '__main__':
    guess_the_number()