drinks = ["아이스 아메리카노","카페 라떼","커피","카푸치노","샌즈 커피"]
prices=[1500,2500,1000,3000,5000]
amount = [0] * len(drinks)
totalPrice=[0]
menu_text = ""

def get_menu_text(drinks , prices):
    #menu_text = ""
    # for i in range(len(drinks)):
    #     menu_text += f"{i+1}) {drinks[i]} {prices[i]}원  "
    menu_text= "=======================\n"
    menu_text +="\n".join([f"{i+1}) {drinks[i]} {prices[i]}원  " for i in range(len(drinks))])
    menu_text += f"\n{len(drinks)+1}) 주문 종료 \n"
    return menu_text


def choice_menu(menu: str, totalPrice :int ) ->tuple[int, bool]:
    try:
        nMenu = int(menu)
        if 1 <= nMenu <= len(drinks):
            index = nMenu - 1
            amount[index] += 1
            print(f"{drinks[index]}를 주문하셨습니다. 가격은 {prices[index]}원 입니다. {amount[index]}개 주문하셨습니다.\n")
            totalPrice[0] += prices[index]
            return totalPrice, False  # 계속 주문
        elif nMenu == len(drinks) + 1:
            print("주문을 종료합니다.")
            return totalPrice, True  # 주문 종료
        else:
            print(f"{menu}번은 없는 메뉴입니다.")
    except ValueError:
        print("숫자로 입력해주세요.")

    return totalPrice, False

def result_Receipt(totalPrice):
    print(f"{'상품명':^20}{'단가':^6}{'수량':^6}{'금액':^10}")
    for i in range(len(drinks)):
        if amount[i] <= 0:
            pass
        else:
            print(f"{drinks[i]:^20}{prices[i]:^6}{amount[i]:^6}{prices[i] * amount[i]:^10}")
    print(f"총 가격:{totalPrice}")

