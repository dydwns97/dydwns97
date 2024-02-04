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

print("가위바위보 게임을 시작합니다@@@!.")
game_images = [rock, paper, scissors] 
import random
# User input
user_choice = int(input("What do you choose? Type 0 for 주먹, 1 for 보 or 2 for 가위. "))
if user_choice > 2:
  print("잘못입력했습니다. 0, 1, 2 중에 다시 골라 주세요!!.")
else:
  print("User chose: ")
  user_choice = int(user_choice)
  print(game_images[user_choice])  
  
# 컴퓨터 차례
  print("Computer chose: ")
  computer_choice = random.randint(0,2)
  print(game_images[computer_choice])

# 승패 결정
  if user_choice == 0 and computer_choice == 2:
    print("승리하였습니다!!!!.")
  elif user_choice == 1 and computer_choice == 0:
    print("승리하였습니다!!!!.")
  elif user_choice == 2 and computer_choice == 1:
    print("승리하였습니다!!!!.")
  elif user_choice == computer_choice:
    print("무승부입니다!!.")

  else:
    print("당신이 패배하였습니다.ㅜㅜ")
  
