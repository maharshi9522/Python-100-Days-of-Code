import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("The Rock Paper Scissor Game")
print("Let's Begin!")
list=[rock,paper,scissors]
print("Enter your choice 0:rock,1:paper,2:scissors")
user_choice=int(input())
print("You chose/n",list[user_choice])
comp_choice=random.randint(0,2)
print("Computer chose/n",list[comp_choice])
if comp_choice==user_choice:
    print("It's a Draw!")
elif (comp_choice==0 and user_choice==2) or (comp_choice==2 and user_choice==1) or (comp_choice==1 and user_choice==0) :
    print("You loose")
else:
    print("You win .Congrats!")
