""""""
"""
날짜 관련
datetime 이라는 모듈
모듈: 하나 이상의 파이썬 파일이 있는 폴더
"""
# import datetime.datetime        # A.B A폴더에서 파일 혹은 클래스 혹은 함수를 import
# datetime.datetime.now();

from datetime import datetime   # from A import B
now = datetime.now()    # 현재시각을 구해서 datetime 객체로 저장
# print(type(now))
"""
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.date())
"""
# 올해가 윤년인지 판단하는 프로그램
this_year = now.year
# 1) 연도가 4로 나누어 떨어지면 윤년
# 2) 연도가 100으로 나누어 떨어지면 윤년이 아님
# 3) 연도가 400으로 나누어 떨어지면 윤년

if this_year%400==0:
    print("윤년이 맞습니다.")
elif this_year%100==0:
    print("윤년이 아닙니다.")
elif this_year%4==0 :
    print("유년이 맞습니다.")
else:
    print("윤년이 아닙니다.")

if this_year%400==0 or (this_year%100!=0 and this_year%4==0):
    print("윤년이 아닙니다.")
else:
    print("윤년이 맞습니다.")
