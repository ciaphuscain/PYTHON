
import random

l1=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
l2=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

random.shuffle(l1)
random.shuffle(l2)
encryption_key={}
for i in range(len(l1)):
    encryption_key[l1[i]]=l2[i]
decryption_key={}
for i in encryption_key.items():
    decryption_key[i[1]]=i[0]
print(encryption_key)
print(decryption_key)
def encryption():
    choice= 'deeecrypt'
    match choice.lower():
        case 'encrypt':
            encrypted_messgae=''
            message=input('enter the message')
            messagelist=list(message)
            messagelist1=list()
            for i in messagelist:
                messagelist1.append(encryption_key[i])
            encrypted_messgae=''
            for i in messagelist1:
                encrypted_messgae+=i
            print(encrypted_messgae)

        case 'decrypt':
            message=input('enter the message')
            decrypted_messgae=''
            messagelist=list(message)
            messagelist1=list()
            for i in messagelist:
                messagelist1.append(decryption_key[i])
            encrypted_messgae=''
            for i in messagelist1:
                decrypted_messgae+=i
            print(decrypted_messgae)
        case _:
            while choice not in ['encrypt','decrypt']:
                print('please answer the question with a valid answer')
                choice= input('do you want to encrypt or decrypt: ')
                

continuee=input('do you want to continue(y/n):')
if  continuee.lower()=='y':
    encryption()
elif continuee.lower()=='n':
    print('Thank you')
else:
    while continuee not in ['y','n']:
        pprint('please answer the question with a valid answer')
        continuee=input('do you want to continue(y/n):')
'''
needs polishing
'''