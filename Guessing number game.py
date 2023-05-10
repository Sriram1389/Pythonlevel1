import random
fix = random.randint(1,9)

while True:
    i=1
    while i<=3:
        guess = int(input('Guess the number'  ))
        if fix == guess:
                print('you won the game')
                break
        else:
            print('wrong guess')
            i=i+1
    else:
        print('you lost the game')

    x=input('Do you need to play again(yes\no):')
    if x == 'no':
      break
print ('Gamee over')
