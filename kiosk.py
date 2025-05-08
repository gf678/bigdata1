drinks = ["아이스 아메리카노","카페 라떼","커피","카푸치노","샌즈 커피"]
prices=[1500,2500,1000,3000,5000]
amount = [0] * len(drinks)
totalPrice=0
menu_text = ""

DISCOUNT_THRESHOLD = 10000 #const
DISCOUNT_RATE = 0.1 #할인율

def apply_discount(total: int) ->float:
    if total >=DISCOUNT_THRESHOLD:
        return  total*(1-DISCOUNT_RATE)
    return total

def get_ticket_number() -> int:
    try:
        with open("ticket.txt","r") as fp:
            number = int(fp.read())
    except FileNotFoundError:
        number=0

    number=number+1

    with open("ticket.txt","w") as fp:
        fp.write(str(number))

    return number

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
            totalPrice += prices[index]
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

    discount_price=apply_discount(totalPrice)
    discount= totalPrice-discount_price

    if discount>0:
        print(f"총 가격:{totalPrice}")
        print(f"할인 금액:{discount}")
        print(f"할인 적용후 지불하실 금액:{discount_price}")
        print(f"번호표:{get_ticket_number()}")
    else:
        print(f"할인이 적용되지 않았습니다.")
        print(f"총 가격:{totalPrice}")

