# height = float(input())
# weight = int(input())

# BMI = weight / (height**2)

# if BMI < 18.5:
#   print("Your BMI is {}, you are underweight.".format(BMI))
# elif BMI < 25:
#   print("Your BMI is {}, you have a normal weight.".format(BMI))
# elif BMI < 30:
#   print("Your BMI is {}, you are slightly overweight.".format(BMI))
# elif BMI < 35:
#   print("Your BMI is {}, you are obese.".format(BMI))
# else:
#   print("Your BMI is {}, you are clinically obese.".format(BMI))

print("Thank you choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L")

bill = 0

#첫번쨰로 사이즈 선택
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25
#두번쨰로 페퍼로니 추가
add_pepperoni = input("Do you want pepperoni? Y or N")
if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
        
    else:
        bill = bill + 3
        
#세번쨰로 치즈추가
extra_cheese = input("Do you want extra cheese? Y or N")
if extra_cheese == "Y":
    bill = bill + 1
    
print("Your final bill is: ${}.".format(bill))