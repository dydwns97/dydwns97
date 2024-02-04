line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?") 

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
num_letter = int(position[1]) - 1
map[num_letter][letter_index] = "X"
#약간 헷갈렸지만, abc.index()를 통해 [a b c] 이 문자열에 수를 셌다. [0]=a => 숫자로 변환하는것이다.
#map[num_letter]가 먼저와야 한다 왜냐면 b3이라고 입력시에 3 - 1 = 2 = line3이기 떄문에 거의 숫자가 맨 앞으로 해주어야한다.
print(f"{line1}\n{line2}\n{line3}")