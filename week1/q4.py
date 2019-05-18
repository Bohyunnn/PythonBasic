# BMI 수치구하기
# BMI = 체중 / 신장^2
# meter로 환산
try:
    height = input('키를 입력해주세요: ')
    height = float(height)
    weight = input('몸무게를 입력해주세요: ')
    weight = float(weight)
    BMI = (weight)/((height**2/10000))
    print(BMI)
except:
    print('정수만 입력해주세요.')
    # 아무것도 안하고 넘어갈때는 pass


# 1) 여러명의 BMI 수치를 입력받아 계산하고 싶다 -> 반복문
# 2) BMI 수치로 비만, 정상, 저체중을 판별 할 수 있다 -> 조건문 if-else
# 3) 오류 처리 -> try - except


