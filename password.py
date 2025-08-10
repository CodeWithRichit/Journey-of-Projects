def chec_password_strength():
    while True:
        cons=input('Hey!Do you wanna check strength of your password, (Y/N/Quit): ').lower()
        if cons=='y':
         u_inp=input('Enter your password: ')
         if len(u_inp)<7:
            print('Weak,Increase the length of the password👎')
         elif len(u_inp)>=7 and u_inp.isalnum() and not u_inp.isdigit() or u_inp.isalpha():
            print('Medium,Use special characters also👍')
         else:
            print('Strong🔥')
        elif cons=='quit':
         exit()
        else:
         print('See you,next time!')
         break
    print('Thanks alot!')
chec_password_strength()
    
          