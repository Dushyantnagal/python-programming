from random import *

computer_num = randrange(1, 101)
score=10
while True:
    user_num = int(input('Guess the number between 1 and 100'))
    if user_num==computer_num:
        print('You Win with score', score)
        break
    elif user_num> computer_num:
        print('Too Large')
    else:
            print('Too Small')
    score-= 1
        
