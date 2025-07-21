counter = 0
import random
x = int(input("enter the min number: "))
y = int(input("enter the max number: "))
number = random.randint(x, y)
while True:
    human_number = int(input("use your luck and enter the number:"))
    if human_number == number:
        print("wow you are so lucky")
        break
    elif human_number > number:
        print("the number is smaller")
        counter += 1
    elif human_number < number:
        print("the number is bigger")
        counter += 1
    if counter == 5:
        print("you 5 try and all of them is end ")
        break
#بازي حدس اعداد