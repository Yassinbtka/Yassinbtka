import  random , os , time
import  colorama
from  colorama import  Back, Fore ,Style



def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:

        guess=int(input(f'Guess Number (Between 1 and {x}):'))
        if guess > random_number:
            # IF  your system is (Linux or Mac) you can change 'cls' to 'clear' !!!!
            os.system('cls')
            print('Sorry , guess again. Too high.')

        elif guess < random_number:
            os.system('cls')
            print('Sorry , guess again. Too low')
    os.system('cls')

    print('***********************************************************\n')
    print(f'Yah, Corrects. You have guessed the number {random_number} correctly!!\n')
    print('***********************************************************')
def computer_geuss(x):

    print(f'Guess number between 1 and {x}\n')
    print('5 seconds ...')
    time.sleep(5)
    os.system('cls')
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        guess = random.randint(low,high)
        os.system('cls')
        feedback=input(' Is =>>' + Fore.YELLOW + f' {guess} '+ Fore.LIGHTWHITE_EX + ' too high (high), or lo w(low) or correct (correct):').lower()
        if feedback == 'high':

            high = guess - 1
        elif feedback=='low':

            low= guess +1
        elif feedback=='correct':
            os.system('cls')
            print(f'Yay I geusses your number {guess},correctly!!')
            return


# guess(10)
# computer_geuss(10)

print("if you want computer guesses your number click => 1 ")
print("if you want  guesses  number Computer  click =>  2 ")
number_game = int(input("Entre: "))
if number_game == 1:
    computer_geuss(10)
elif number_game == 2:
    guess(10)
else:
    print(input("pleas click 1 or 2 : "))

