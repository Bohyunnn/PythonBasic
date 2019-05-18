# [연산]
# 1. 산술 연산: 사칙연산, 특수연산
# 2. 문자열 연산: +, *

name = "Bohyun"
# 1) 문자열의 덧셈
msg = "Hello " + name   # name이라는 값의 문자열 값이 복사되어 저장된게 아니라 한 메모리 안에 저장되어 놓은 걸 가져오는 것
print(msg)

greeting = input("인사말을 입력해주세요: ")
name = input("이름을 입력해주세요: ")
print(greeting, name)

# 2) 문자열의 곱셈: 문자열을 반복하여 붙인다.
print("Hello"*7)

# 연산의 오버라이딩: 내가 만든 데이터 타입의 연산을 정의할 수 있다.

# 산술 연산: 사칙연산
# 덧셈, 뺄셈, 곱셈, 나눗셈
number1 = 10
number2 = 7
number3 = number1 * number2

# 선택 실행: alt+sh+e
# 산술연산: 특수연산
# **, %, //
print(4**2)  # 3의 2승
print(3%2)   # 나머지 - 정수
print(10//2)  # 나눗셈의 몫 - 정수

# type(~): 변수 타입 알아내는 함수
# str: string 문자열
# int: integer 정수
# float: floating number 실수

# 문법오류 : 실행x, 오타나 실제 문법 자체가 틀린 경우
# 논리오류 : 실행은 되나 결과가 엉망
# 런타입오류 : 실행은 되나 결과가 이상해지면서 프로그램이 종료
number1 = input('첫번째 숫자를 입력해주세요: ')
print(type(number1))    # 논리오류 -> 숫자가 아니라 문자열
# 어떤 데이터를 다른 형태의 데이터로 바꾸는것 => Type Casting(형변환)
number2 = input('두번째 숫자를 입력해주세요: ')
print(type(number2))
number3 = int(number1) + int(number2)
print(number3)

# 연산자의 우선 순위
# ()
# **
# *,/,%,//
# +, -
