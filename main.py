MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
machin_on = True

resources = {"water": 1000,
            "milk": 500,
            "coffee": 100
            }
profit = 0



#TODO 코인 함수 정의, 차감
def machine(coffee_guess, menu):
    global machin_on, profit
    print("please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01

    pay = round(quarters + dimes + nickles + pennies, 2)
    total = round(pay - float(menu["cost"]), 2)

    if pay < menu["cost"]:
        print(f"총 금액:{pay}$ 받았습니다. 금액이 충족하지 않습니다. 다시 넣어주세요!!.")
    else:
        print(f"총 금액:{pay}$ 받았습니다. {coffee_guess} 나왔습니다. 맛있게 드세요!!. 거스름돈은 {total}$입니다.")
        profit += menu["cost"]

#TODO 재료 차감
        for item in menu['ingredients']:
            resources[item] -= menu['ingredients'][item]
        machin_on = False

#TODO report(재료)의 정의 및 머신 작동
    # 시작
while machin_on:
    guess = input("무엇을 원하십니까? ('espresso', 'latte', 'cappuccino'): ").lower()

    if guess not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("'espresso', 'latte', 'cappuccino'중 한가지를 골라주세요!.")
    elif guess == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif guess == "off":
        machin_on = False
    else:
        menu = MENU[guess]
        machine(guess, menu)  # machine 함수 호출 시에 커피 이름과 메뉴 정보를 전달






