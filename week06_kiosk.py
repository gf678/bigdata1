drinks = ["아이스 아메리카노","카페라떼","커피","카푸치노"]
prices=[1500,2500,1000,3000]
amount=[0,0,0,0]
totalPrice=0
menu_text = ""

while True:
    menu_text = "" #문자열 초기화
    for i in range(len(drinks)): # 음료 개수만큼의 메뉴 띄우기 반복
        menu_text += f"{i+1}) {drinks[i]} {prices[i]}원  "
    menu_text += f"{len(drinks)+1}) 주문 종료 >> " #마지막 종료 띄우기

    menu = input(menu_text) #숫자넣기

    if menu.isdigit(): #숫자 맞어? 검출기
        num = int(menu) #문자열을 정수형으로 변환
        if 1 <= num <= len(drinks):
            index = num - 1
            print(f"{drinks[index]}를 주문하셨습니다. 가격은 {prices[index]}원 입니다.")
            totalPrice += prices[index]
            amount[index] += 1  #음료 개수만큼의 메뉴 리뷰
        elif num == len(drinks) + 1:
            print("주문을 종료합니다.")
            break   #주문종료
        else:
            print(f"{menu}번은 없는 메뉴입니다.") #잘못고름
    else:
        print("숫자로 입력해주세요.")    #숫자아님

for i in range(len(drinks)):
    if amount[i] <=0:
        pass
    else:
        print(f"{drinks[i]} {prices[i]}원 {amount[i]}잔 총 {prices[i]*amount[i]}잔")
print(f"총 가격:{totalPrice}")