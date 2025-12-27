import random
choices=['stone','paper','scissor']
while True:
    pc_choice = random.choice(choices)
    user_choice = (input("enter your choice: "))
    if user_choice==pc_choice:
        print("pc guess=",pc_choice)
        print("clash")
        continue
    elif (pc_choice=='stone'and user_choice=='scissor') or (pc_choice=='scissor' and user_choice=='paper') or (pc_choice=='paper' and user_choice=='stone'):
        print("pc guess=", pc_choice)
        print("you lose")
        continue
    elif (pc_choice=='stone' and user_choice=='paper') or (pc_choice=='paper' and user_choice=='scissor') or (pc_choice=='scissor' and user_choice=='stone'):
        print("pc guess=", pc_choice)
        print("you win")
        break
    else:
        print("invalid input")
        continue
