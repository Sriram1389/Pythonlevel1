state = 'stopped'
while True:
    print('1.start')
    print('2.stop')
    print('3.Exit')
    ch=int(input('Choose the option:'))
    if ch==1:
        if state =='stopped':
            print('car is started')
            state = 'started'
        else:
            print ('car is already started')
    elif ch==2:
         if state =='started':
            print('car is stopped')
            state = 'stopped'
         else:
            print ('car is already stopped')
    elif ch==3:
         print('Game over')
         break
    else:
        print('Check your input')
        
