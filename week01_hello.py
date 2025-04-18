# name = input("이름 입력 : ")
# print(f"{name}님 환영합니다!")
# # alt + shift + F10

a = int(input())
b = int(input())

try :
    print(a/b)
except ZeroDivisionError:
    print("do not div zero")