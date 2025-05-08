from kiosk import get_ticket_number, result_Receipt, get_menu_text ,drinks ,prices ,choice_menu ,totalPrice

while True:

    menu = input(get_menu_text(drinks,prices)) #숫자넣기
    totalPrice, is_done = choice_menu(menu, totalPrice)
    if is_done:
        break

result_Receipt(totalPrice)