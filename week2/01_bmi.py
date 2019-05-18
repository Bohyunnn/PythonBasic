while True:
    weight = input("몸무게를 입력해주세요. : ")
    try:
        weight = float(weight)
        if weight > 0 :
            break
    except:
        print("입력값이 올바르지 않습니다.")

while True:
    height = input("키를 입력해주세요. : ")
    try:
        height = float(height)
        if height > 0 :
            break
    except:
        print("입력값이 올바르지 않습니다.")

bmi = (weight) / ((height ** 2 / 10000))
print(bmi)

# bmi 수치는 22..05 이고 체중 등급은 정상체중입니다.
if bmi < 18.5:
    level = "저체중"
elif bmi >= 18.5 and bmi < 23 :  #  18.5 <= bmi < 23 가능 ---> chaunung comparison
    level = "정상"
else:
    level = "고체중"

format_string = "bmi 수치는 %0.2f 이고 체중 등급은 %s입니다."
msg = format_string % (bmi, level)
print(msg)

"""
if 조건1 and 조건2 :  조건1이 거직이라면 조건2는 판별하지 않는다.
if 조건1 or 조건2  :  조건1이 참이라면 조건 2는 판별하지 않는다. 
"""


"""
타입의 명시적 선언
str_bmi_level
bmi_level = "1"
var bmi_lvel:str;
bmi_level = "2"
"""

# 변수의 선언과 초기화를 동시에 해야한다.
# 타입의 암시(묵시)적 선언
bmi_level = ""
"""
데이터 타입을 쓰는 언어들에 강타입, 약타입
* 파이썬으로 프로그래밍 할 때도 타입을 지정해서 쓰는 경우도 있다.
"""
