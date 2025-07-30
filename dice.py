# import random

# while True:
#     dice_1=input('Enter an option (y/n): ').lower()
#     if dice_1=='y':
#         choice=int(input('Enter number of dice from 1 to 5:'))
        # if choice==1:
        #      dice_4=random.randint(1,6)
        #      print(dice_4)
        # elif choice==2:
        #     dice_2=random.randint(1,6)
        #     dice_3=random.randint(1,6) 
        #     print((dice_2,dice_3))       This is hardcode,instead see the solution below
        # elif choice==3:
        #     dice_2=random.randint(1,6)
        #     dice_3=random.randint(1,6) 
        #     dice_4=random.randint(1,6)
        #     print((dice_4,dice_2,dice_3))
        # elif choice==4:
        #     dice_2=random.randint(1,6)
        #     dice_3=random.randint(1,6) 
        #     dice_4=random.randint(1,6)
        #     dice_5=random.randint(1,6)
        #     print((dice_5,dice_2,dice_3,dice_4))
        # elif choice==5:
        #      dice_2=random.randint(1,6)
        #      dice_3=random.randint(1,6) 
        #      dice_4=random.randint(1,6)
        #      dice_5=random.randint(1,6)
        #      dice_6=random.randint(1,6)
        #      print((dice_5,dice_3,dice_2,dice_4,dice_6))
    #     else:
    #         print('Please enter value inside [1,5]')
    # elif dice_1=='n':
    #     print('Thanks for playing')
    #     break
    # else:
    #     print('Invalid value entered')
import random

count=0
while True:
    throw=input('Enter an option (y/n): ').lower()
    if throw=='y':
        count=count+1
        choice=int(input('Choose the number of dice,you want to play with btw [1,100]: '))
        if 1<=choice<=100:
            roll=[]
            for i in range(choice):
                roll.append(random.randint(1,6))
            print('Dice roll:',roll)
        else:
            print('Enter value inside [1,100]')
    elif throw=='n':
        print('You rolled the dice:',count,'times')
        print('Thanks for playing')
        break
    else:
        print('Enter valid alphabet')
