# count=0
# while True:
#     try:
#         guess=int(input('Guess a number between [1,100]: '))
#         count=count+1
#         if guess==88:
#              print("Congrats,that's the correct answer." ) #If you have a predecided number to tell then do this either follow the below code
#              print('You took a total of,',count,'tries to win the game')
#              break
#         elif guess>88:
#             print('Your answer is higher than the correct number')
#         else: 
#           print('Your answer is lower than the correct number')
#     except ValueError:
#      print('Please,Input a number between [1,100]')
import random
count=0
generate_random_number=random.randint(1,100)
while True:
    try:
        User_input=int(input('Guess a number between [1,100]: '))
        count=count+1
        if User_input>generate_random_number:
            print('Your guess is higher than the correct number.')
        elif User_input<generate_random_number:
            print('Your guess is lower than the correct number.')
        else:
            print('Congrats,You guessed it.')
            print('You took',count,'tries')
            break
    except ValueError:
        print('Error:Please,enter a value between (1,100)')
