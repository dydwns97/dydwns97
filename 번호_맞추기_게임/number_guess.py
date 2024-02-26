#번호 맞추기 게임:


# Include an ASCII art logo.
import random
from art import logo
# numbers = random.randint(1, 100) 여기다 두게 되면 계속 새로운 난수를 입력하게 되어 계속 숫자가 랜덤으로 바뀐다...;;;;
end_of_game = False

def start():

    print(logo)
    print("@@환영합니다!. 번호 맞추기 게임입니다!@@")
    print("I'm thinking of a number between 1 and 100.")

    difficult()

def game_start(numbers, lives):
    global end_of_game
    while not end_of_game:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > numbers:
            lives -= 1
            print("Too high.")
            print("Guess again.")
            
        elif guess < numbers:
            lives -= 1
            print("Too low.")
            print("Guess again.")
        else:
            print(f"You got it!! The answer was {numbers}.")
            end_of_game = True

        if lives == 0:
            print(f"Game Over......answer was {numbers}.")
            end_of_game = True

def difficult():
    global end_of_game  
    while not end_of_game:   
        
        dif = input("난이도를 선택하십시오. 'easy' or 'hard': ").lower()
        if dif == 'easy':
            lives = 10
            numbers = random.randint(1, 100)
            game_start(numbers, lives)
            end_of_game = True

        elif dif == 'hard':
            lives = 5
            numbers = random.randint(1, 100)
            game_start(numbers, lives)
            end_of_game = True

        else:
            print("잘못입력하셨어요!! 다시 난이도를 선택해주세요.")

# while true로 한다면 처음에 'y'를 입력하면 계속 'y'가 입력되어서 무한반복이 일어난다!!
restart = input("번호 맞추기 게임을 시작하시겠습니까? 'y' or 'n': ")
while restart == 'y': #반복문을 써서 restart 반복되게 만들어 'y'가 입력되면 start()로 'n'이 입력된다면 false로 인해 print()가 출력됨.
    start()
    restart = input("게임을 다시 시작하시겠습니까? 'y' or 'n': ")

print("수고하셨습니다.")



