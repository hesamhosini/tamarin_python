import random
import time

score = 0

def p():
    global score
    number1 = random.randint(0, 1000)
    number2 = random.randint(1, 1000)  
    operators_list = ["*", "-", "+", "**", "/"]
    operators = random.choice(operators_list)

 
    if operators == "**":
        number2 = random.randint(0, 5)

    print("Please answer to the following quiz")

    try:
        human_answer = input(f'{number1} {operators} {number2} = ')


        human_answer = float(human_answer)

    except ValueError:
        print("Invalid input! Please enter a number.")
        print("---------------------------")
        return


    if operators == "*":
        answer = number1 * number2
    elif operators == "+":
        answer = number1 + number2
    elif operators == "-":
        answer = number1 - number2
    elif operators == "**":
        answer = number1 ** number2
    elif operators == "/":
        answer = number1 / number2


    if operators == "/":
        if abs(human_answer - answer) < 0.01: 
            score += 1
            print("Good job, you are very smart!")
        else:
            print(f"Wrong answer! Correct answer is {answer:.2f}")
    else:
        if human_answer == answer:
            score += 1
            print("Good job, you are very smart!")
        else:
            print(f"Wrong answer! Correct answer is {answer}")

    print("---------------------------")

while True:
    p()
