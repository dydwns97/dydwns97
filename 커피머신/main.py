from menu import Menu, MenuItem

from coffee_maker import CoffeeMaker

from money_machine import MoneyMachine

# 코드를 짜보자 천천히
# 먼저 객체를 생성하자.
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#커피 머신을 만들자(새로운 변수를 만들자)
def order_play():
    global play
    #사용가능한 메뉴 출력
    print("다음 메뉴 중에 고르시오.")
    print(menu.get_items())

    #메뉴 질문
    order_name = input("어떤 메뉴를 선택하시겠어요?: ").lower()
    if order_name in menu.get_items():
        #주문한 커피 정보 가져오기
        order = menu.find_drink(order_name)
        #재료가 충분한지 확인
        if coffee_maker.is_resource_sufficient(order):
            #돈 지불하기
            if money_machine.make_payment(order.cost):
                #커피제조하기
                coffee_maker.make_coffee(order)


    elif order_name == 'off':
        play = False

    elif order_name == 'report':
        coffee_maker.report()
    else:
        print("잘못입력하셨습니다. 다시 주문해주세요.")

#자판기 무한 반복
play = True
while play:
    order_play()







