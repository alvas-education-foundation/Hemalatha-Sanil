print('Enter correct username and password combo to continue')
count=0

while count<3:
    username=input('Enter username: ')
    password=input('Enter password: ')
    if password !='e3$WT89x' or username !='Micheal':
        print('Invalid username or Password')
        count+=1
    elif password=='e3$WT89x' and username=='Micheal':
        print('You have succesfully login')
    
        
    while count==3:
        print('Account locked')
        break