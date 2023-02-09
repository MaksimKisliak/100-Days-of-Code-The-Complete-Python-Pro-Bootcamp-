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

#Write your code below this line 👇
human_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors:'))
array = [rock, paper, scissors]
import random
random_comp_choice = random.randint(0,2)
print (f'Your choice:\n{array[human_choice]}\nComputer\'s choice:\n{array[random_comp_choice]}')
if human_choice == random_comp_choice:
    print('Draw')
elif human_choice > random_comp_choice:
    print('You lose')
elif (human_choice == 0 and random_comp_choice == 2) or (human_choice == 1 and random_comp_choice == 0) or (human_choice == 2 and random_comp_choice == 1):
    print('You win')
else:
    exit()
