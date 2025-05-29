# ddl create (created_at field)
# dml update -> insert
import requests
import kiosk as kk

if __name__ == "__main__":
    url = f"https://wttr.in/london?format=2"
    #url = f"https://wttr.in/london?format=%C+%t&lang=ko"
    #url = f"https://naver.com/kim"
    try:
        response=requests.get(url)
        if response.status_code ==200:
            print(response.text.strip())
        else:
            print(f"상태 코드 :{response.status_code}")
    except Exception as err:
        print(f"오류 : {err}")
    kk.run()
    kk.result_receipt()
    kk.print_ticket_number()
