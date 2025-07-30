from random import choice
while True:
    
        comp_choice=choice(['rock','paper','scissor'])
        user_input=input('Enter any one from (Rock,Paper,Scissor): ').lower()
        if user_input =='rock':
          print('Computer: ',comp_choice)
        elif user_input == 'paper':
          print('Computer: ',comp_choice)
        elif user_input=='scissor':
            print('Computer: ',comp_choice)
        else:
           print('Please enter a choice from upper three only')
        if (user_input=='rock' and comp_choice=='scissor') or (user_input=='scissor' and comp_choice=='paper') or (user_input=='paper' and comp_choice=='rock'):
            print('You win')
        elif ((user_input=='scissor' and comp_choice=='rock') or (user_input=='paper' and comp_choice=='scissor') or (user_input=='rock' and comp_choice=='paper')):
            print('You lose')
        else:
            print('Tie!')
            
        if (user_input=='rock' and comp_choice=='scissor') or (user_input=='scissor' and comp_choice=='paper') or (user_input=='paper' and comp_choice=='rock'):
            consent=input('Do you want to play further?Say(Yes/No): ').lower()
            if consent=='yes':
                continue
            elif consent=='no':
                break
            else:
                print('Please reply,either "Yes" or "No"')