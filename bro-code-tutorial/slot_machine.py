import random
icons=['A','B','C','D']
while  True:
    print('*************************************************************************')
    print('welcome to the game !!')
    amount=float(input('Enter the amount you want to play with:'))
    while True:
        bet=float(input('pleace your bets')) 
        if bet > amount:
                print('you dont have that money' )
        elif  bet<= amount:
                amount-=bet
                _1stcolumn=random.choice(icons)
                _2ndccolumn=random.choice(icons)
                _3rdcolumn=random.choice(icons)
                print(_1stcolumn,_2ndccolumn,_3rdcolumn)
                if _1stcolumn==_2ndccolumn==_3rdcolumn=='A':
                    print('jackpot')
                    amount*=20
                elif _1stcolumn==_2ndccolumn==_3rdcolumn=='B':
                    print('luck seems to be on your side')
                    amount*=10
                elif _1stcolumn==_2ndccolumn==_3rdcolumn=='C':
                    print('luck seems to be on your side')
                    amount*=5
                elif _1stcolumn==_2ndccolumn==_3rdcolumn=='D':
                    print('luck seems to be on your side')
                    amount*=2
                else:
                    print('better luck next time' )
        continue_=input('do u want to continue?(Y/N)')
        while continue_.upper() not in ['Y','N']:
            print('please enter a valid input')
            continue_=input('do u want to continue?(Y/N)')
        if continue_=='Y':
            pass
        else:
            print('thanks for playing')
            print(f'final amount is {amount}')
            break
'''
needs polishing
'''