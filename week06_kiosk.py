menus = ["아이스 아메리카노","카페라떼","커피"]
prices=[1500,2500,1000]
amount=[0,0,0]
totalPrice=0
while True:
    menu = input(f"1) {menus[0]} {prices[0]}원  2) {menus[1]} {prices[1]}원  3) {menus[2]} {prices[2]}원  4) 주문 종료 >> ")

    if menu in ["1", "2", "3"]:
        index = int(menu) - 1
        print(f"{menus[index]}를 주문하셨습니다. 가격은 {prices[index]}원 입니다.")
        totalPrice += prices[index]
        amount[index] += 1
    elif menu == "4":
        print("주문을 종료합니다.")
        break
    else:
        print(f"{menu}번은 없는 메뉴입니다.")

for i in range(len(menus)):
    print(f"{menus[i]} {prices[i]}원 {amount[i]}잔 총 {prices[i]*amount[i]}잔")
print(f"총 가격:{totalPrice}")