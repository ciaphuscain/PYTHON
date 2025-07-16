#assignment 1  
user_name="sivakarthigeyen"
year=2025
pi=22/7
is_admin=True
print(f"my name is {user_name}")
print(f"the year is {year}")
print(f"pi is still somewhere around {pi}")
if is_admin:
    print('iam the admin')

#typecasting
'''L= [user_name,year,pi,is_admin]
for i in L:
    print(type(i))

print(int(pi))
print(bool(pi))
'''
#intput()
'''name=input("what is your name:")
age=input("what is your age:")

print(f"let me get this straight, you are {name} and you are {age} years old")

print(type(age))'''


#exersice 1
print('this is to measure the area of a rectangle')
lenght=input('enter length of rectangle: ')
breadth=input('enter the breaadth of the rectangle:')
area=float(lenght)*float(breadth)
print(f'area is {area} unit²')

#exersice 2

print('shopping cart programm')
number=int(input('how many unique items are there in yor shopping cart: '))
total=0
list_of_items_and_prices={}
for i in range(number):
    item=input('enter item name: ')
    price=float(input('enter induvidual item price:'))
    quantity=int(input('enter quantity:'))
    temp=price*quantity
    list_of_items_and_prices[item]=temp
    total+=temp
print(' you brought the following')
for i in list_of_items_and_prices: 
    print(f'{i} for {list_of_items_and_prices[i]} ')
print(f'bringing the total to: {total}')

'''note that i used my school knowledge to make it a dictionary'''