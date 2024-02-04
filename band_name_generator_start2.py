print("Welcome to the band name generator")
genre = input("어떤 장르의 음악을 하는 밴드를 만들고 싶나요?\n")
city = input("당신이 사는 곳은 어디인가요?\n")
name = input("밴드 이름은 무엇으로 할건가요?\n")
Ask = "{0} {1} {2}".format(genre, city, name)
print("Your band name could be" + ' ' + Ask)

# 문자열 포맷팅
# format을 활용해서 공백을 만들었다. / 이것 말고 ' '을 활용해서도 사용가능하다.