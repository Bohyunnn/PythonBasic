""""""
"""
연습문제 6.퇴직 계산기
현재 나이와 퇴직을 하고 싶은 나이를 입력하면 올해로부터 계산하여 퇴직 연도를 출력하시오
입출력 예시 :
입력 화면 – 현재 나이를 입력하세요 : 20
            퇴직을 원하는 나이를 입력하세요 : 50
출력 화면 – 당신은 앞으로 30 년 뒤에 퇴직을 하게 됩니다.
            올해는 2018 년이므로 2048 년이 퇴직을 하는 해 입니다.
            (수치 계산과 날짜 계산이 필요합니다. - datetime 을 사용하여 현재 년도를 알아내야 합니다)
"""

from datetime import datetime
now_year = datetime.now().year

while True:
    while True:
        age = input("현재 나이를 입력하세요. : ")
        try:
            age = int(age)
            break
        except:
            print("제대로 입력해주세요.")
    while True:
        retire_age = input("퇴직을 원하는 나이를 입력하세요. : ")
        try:
            retire_age = int(retire_age)
            break
        except:
            print("제대로 입력해주세요.")
    retire_after_year = retire_age - age
    if retire_after_year >= 0:
        break
    else:
        print("퇴직을 원하는 나이가 현재 나이보다 적습니다. 다시 입력해주세요.")

retire_year = now_year + retire_after_year
format_string = "당신은 앞으로 {:d}년 뒤에 퇴직을 하게 됩니다.\n올해는 {:d}년이므로 {:d}년이 퇴직을 하는 해 입니다."
msg = format_string.format(retire_after_year, now_year, retire_year)
print(msg)
