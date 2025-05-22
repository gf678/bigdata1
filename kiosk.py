from  datetime import datetime
import sqlite3

drinks = ["아이스 아메리카노","카페 라떼","커피","카푸치노","샌즈 커피"]
prices=[1500,2500,1000,3000,5000]
amount = [0] * len(drinks)
totalPrice=0

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

def print_ticket_number() -> None:
    conn =sqlite3.connect('cafe.db')
    cur =conn.cursor()
    cur.execute('''
        create table if not exists ticket (
        id integer primary key autoincrement,
        number integer not null,
        created_at text not null default (datetime('now', 'localtime'))
        )
    ''')

    cur.execute('select number from ticket order by number desc limit 1')
    result = cur.fetchone()

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if result is None:
        number = 1
        cur.execute('insert into ticket (number, created_at) values (?, ?)', (number, now))
    else:
        number = result[0] + 1
        # cur.execute('update ticket set number=? where id = (select id from ticket order by number desc limit 1)', (number,))
        cur.execute('insert into ticket (number, created_at) values (?, ?)', (number, now))

    conn.commit()
    print(f"번호표 : {number} ({now})")

def get_menu_text() ->str:
    #menu_text = ""
    # for i in range(len(drinks)):
    #     menu_text += f"{i+1}) {drinks[i]} {prices[i]}원  "
    menu_text= "=======================\n"
    menu_text +="\n".join([f"{i+1}) {drinks[i]} {prices[i]}원  " for i in range(len(drinks))])
    menu_text += f"\n{len(drinks)+1}) 주문 종료 \n"
    return menu_text

def run() ->None:
    while True:
        try:
            menu = int(input(get_menu_text()))
            if 1 <= menu <= len(drinks):
                order_process(menu-1)
            elif menu == len(drinks) + 1:
                print("주문을 종료합니다.")
                break
            else:
                print(f"{menu}번은 없는 메뉴입니다.")
        except ValueError:
            print("숫자로 입력해주세요.")


def order_process(index:int) ->None:
    global totalPrice
    print(f"{drinks[index]}를 주문하셨습니다. 가격은 {prices[index]}원 입니다")
    totalPrice = totalPrice + prices[index]
    amount[index] = amount[index] + 1

def result_receipt() ->None:
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
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


