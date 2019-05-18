"""
q02_interest
"""

"""
원금, 연이율, 이자지급횟수, 거치기간(연단위)
최종 원리금 구하기
원리금 = 원금(1+연이율/이자지금횟수)^(이자지금횟수*거치기간) 
"""
"""
프로그램을 무한 반복 시키기
메뉴 구성
1. 원리금 계산하기
2. 프로그램 종료하기
"""
# 사용자가 선택한 메뉴가 1인지 2인지에 따라 일을 나누고 싶다.
# 분기 -> if 구문
# 1번을 선택했을 때 -> 원리금 계산
# 2번을 선택했을 때 -> 프로그램 종료

while True:
    print("---- MENU ----")
    print("1. 원리금 계산하기")
    print("2. 프로그램 종료하기")
    menu = input("메뉴를 선택해주세요.")

    if menu == '1':
        # 원리금 계산 로직
        while True:
            balance = input("원금을 입력해주세요: ")
            try:
                balance = int(balance)
                break
            except:
                print("제대로 입력해주세요.")

        while True:
            interest = input("연이율을 입력해주세요: ")
            try:
                interest = float(interest)
                break
            except:
                print("제대로 입력해주세요.")

        while True:
            number_of_count = input("이자지금횟수을 입력해주세요: ")
            try:
                number_of_count = int(number_of_count)
                break
            except:
                print("제대로 입력해주세요.")

        while True:
            number_of_years = input("거치기간을 입력해주세요: ")
            try:
                number_of_years = int(number_of_years)
                break
            except:
                print("제대로 입력해주세요.")
        # 원리금 = 원금(1+연이율/이자지금횟수)^(이자지금횟수*거치기간)
        final_balance = balance*(1+interest/100/number_of_count)**(number_of_count*number_of_years)

        format_string = "원금 {:15,d}원, 연이율 {:.2f}%, 이자지급횟수 {:d}회, 거치기간 {:d}년하면 최종 원리금은 {:,.3f}원이 됩니다."
        msg = format_string.format(balance,interest,number_of_count,number_of_years, final_balance)

        print(msg)

    elif menu == '2':
        print("프로그램을 종료합니다.")
        exit() #break
    else:
        print("없는 메뉴입니다.")