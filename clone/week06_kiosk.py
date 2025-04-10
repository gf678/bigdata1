menus = ["아이스 아메리카노","카페라떼"]
prices=[1500,2500]
totalPrice=0
while True:
    menu = input (f"1){menus[0]} {prices[0]} 2){menus[1]} {prices[1]} 3)주문 종료")
    if menu == "1":
        print(f"{menus[0]}를 주문하셨습니다. 가격은 {prices[0]}원 입니다.")
        totalPrice = totalPrice+prices[0]
    elif menu == "2":
        print(f"{menus[1]}를 주문하셨습니다. 가격은 {prices[1]}원 입니다.")
        totalPrice = totalPrice + prices[1]
    elif menu == "3":
        print("종료합니다.")
        break
    else :
        print(f"{menus}번은 없는 메뉴입니다.")

print(f"총 가격:{totalPrice}")