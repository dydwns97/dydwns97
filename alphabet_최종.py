alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":    
      shift_amount *= -1
    for char in start_text:
      if char in alphabet:
  #TODO-3: What happens if the user enters a number/symbol/space?
   #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
   #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text += char  # 숫자, 기호 또는 공백은 그대로 end_text에 추가.

    print(f"Here's the {cipher_direction}d result: {end_text}")


#TODO-1: Import and print the logo from art.py when the program starts.
#print()를 써야함!!!!
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    #이렇게 함으로써 shift 값이 항상 0에서 25 사이의 값이 되어 프로그램이 정상적으로 작동합니다

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("게임을 다시 시작 하시겠습니까? Y or N\n").upper()
    if restart != "Y":
        print("수고하셨습니다. 다음에 또 오세요.")
        break
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).
