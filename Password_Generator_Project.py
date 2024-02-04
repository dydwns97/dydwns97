#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# 첫번째 방법으로 코드를 짰었다!>

# last_letters = []
# for random_letters in range(nr_letters):
#     random_index = random.randint(0, len(letters)-1)
#     last_letters.append(letters[random_index])
# # print(''.join(last_letters))

# last_number = []
# for random_number in range(nr_numbers):
#     random_index = random.randint(0, len(numbers)-1)
#     last_number.append(numbers[random_index])
# # print(''.join(last_number))

# last_symbols = []
# for random_symbols in range(nr_symbols):
#     random_index = random.randint(0, len(symbols)-1)
#     last_symbols.append(symbols[random_index])

# # print(''.join(last_symbols))
# passward = ''.join(last_letters + last_number + last_symbols)
# print(f"Your new passward: {passward}")
#두번째 방법
password = ""

for random_letters in range(1, nr_letters+1):
  password += random.choice(letters)

for random_number in range(1, nr_numbers+1):
  password += random.choice(numbers)

for random_symbols in range(1, nr_symbols+1):
  password += random.choice(symbols)
#밑에 처럼 굳이 +를 안해도 하나로 통일해서 해도 가능하다. 위에서 for처음 부분부터 실행이 되기 떄문@
# password = (last_letters + last_number + last_symbols)
print(f"Your new passward: {password}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&

# 각 요소를 담을 리스트 초기화
# password_list = []

# for random_letters in range(1, nr_letters +1):
#   password_list += (random.choice(letters))

# for random_number in range(1, nr_numbers+1):
#   password_list += (random.choice(numbers))

# for random_symbols in range(1, nr_symbols+1):
#   password_list.append(random.choice(symbols))

# random.shuffle(password_list)
# # random.shuffle(password_list)를 사용해 리스트안에 수들을 무작위로 섞었다.

# password = ''
# for char in password_list:
#   password += char
# print(f"Your password {password}")