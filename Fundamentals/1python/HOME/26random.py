import random

x= random.randint(1,6)
y = random.random()

mylist = ['rock','paper','scissors']
z = random.choice(mylist)

cards = [1,2,3,4,5,6,"D","A","R","S","H"]

random.shuffle(cards)

print(cards)