import kiosk

while True:
    menu = input(kiosk.get_menu_text(kiosk.drinks,kiosk.prices)) #숫자넣기
    totalPrice, is_done = kiosk.choice_menu(menu, kiosk.totalPrice)
    if is_done:
        break

kiosk.result_Receipt(kiosk.totalPrice[0])