# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

import random

from art import logo, vs
# 같은 art파일에 있는거는 ,로 사용
from game_data import data


print("인스타그램 팔로우 수가 'higher' or 'lower' 게임에 오신걸 환영합니다.")

def data_random():
   return random.choice(data) 
    #하나로 묶어버리기 위해서 새로운 함수를 만들었다.

#첫번째 compare A 질문과 두번째 against B 질문을 묶자.
def compare(account):
    name = account['name']
    job = account['description']
    country = account['country']
    
    return f"{name}, a {job}, from {country}."

def follower(guess, a_followers, b_followers):
    #true , false를 기준으로!!

    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
    

#게임 정의\
def game():
    print(logo)
    
    score = 0 #초기화 시켜놓고
    reset = True
    account_a = data_random()
    account_b = data_random()
    # a/ b 를 나눠서 각각 data random를 만든다.
    #반복 시작
    while reset:
        account_a = account_b
        account_b = data_random()
        
        while account_a == account_b:
            account_b = data_random()
    
        print(f"Compare A: {compare(account_a)}")
        print(vs)
        print(f"Compare B: {compare(account_b)}")
        
        #질문하기
        guess = input("팔로우 수가 많은 쪽을 선택하시오. Type 'A' or 'B': ").lower()
        #1. guess를 먼저 'a', 'b'인지 선택하고

        if guess in ['a', 'b']: # true, false로 기준을 잡아 이렇게 정리하는게 훨씬 좋고 구분하기가 좋다.
            a_followers = account_a['follower_count']
            b_followers = account_b['follower_count']
        #2. 두번째 if문 안에다가 또 if문을 만들어서 내가 'a'를 선택했으면 그 값으로 진행하는걸 이용
            
# 문자열 a, b를 기준으로하는게 아니라 true, false를 기준으로 잡고 점수를 증가시키거나 게임을 종료해야함.
            
            if follower(guess, a_followers, b_followers):
                score += 1
                print(f"축하합니다. 누적점수: {score}점입니다. 다음도 진행 해주세요!.")
            else:
                print(f"틀렸습니다. 마지막 점수: {score}점.")
                reset = False
        
            
game()



