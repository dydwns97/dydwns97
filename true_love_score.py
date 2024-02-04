print("The Love Calculator is calculating your score...")
name1 = input("What is their name?") 
name2 = input("What is their name?")

count_name1 = (name1 + name2).lower()
t = int(count_name1.count('t'))
r = int(count_name1.count('r'))
u = int(count_name1.count('u'))
e = int(count_name1.count('e'))
result_name1 = t + r + u + e
# ;  count()를 한번에 ('true')를 쓸 수 없어서 하나하나씩 썼다.
count_name2 = (name1 + name2).lower()
l = int(count_name2.count('l'))
o = int(count_name2.count('o'))
v = int(count_name2.count('v'))
e = int(count_name2.count('e'))
result_name2 = l + o + v + e
# lower()를 통해 이름을 소문자로 다 바꾸어 준다. 그리고 count()를 통해 ture / love을 각 각 세어준다.
result_score = int(str(result_name1) + str(result_name2))

if result_score < 10 or result_score > 90:
  print(f"Your score is {result_score}, you go together like coke and mentos.")
elif result_score >= 40 and result_score <= 50:
  print(f"Your score is {result_score}, you are alright together.")
else:
  print(f"Your score is {result_score}.")