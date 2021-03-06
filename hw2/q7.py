""""""
"""
연습문제 7. 직사각형 방의 면적
국제 표준단위인 피트/야드 단위로 입력받고 도량형을 변환하여 출력하시오.
방의 면적을 계산하여 출력하는 프로그램을 작성하시오.
방의 길이와 폭을 피트 단위로 입력받고, 제곱피트와 제곱미터로 면적을 나타내보시오.
입출력 예시 :
입력 화면 –
    방의 길이는 몇 피트 입니까?	15
    방의 너비는 몇 피트 입니까?	20
출력 화면 –
    당신이 입력한 수치는 15, 20 피트입니다.
    면적은
    300	제곱 피트
    27.871	제곱 미터
    입니다.
추가 내용 :
    제곱 미터 = 제곱 피트 * 0.09290304
    입니다.
"""
while True:
    height = input("방의 길이는 몇 피트 입니까? ")
    try:
        height = float(height)
        break
    except:
        print("제대로 입력해주세요.")

while True:
    width = input("방의 너비는 몇 피트 입니까? ")
    try:
        width = float(width)
        break
    except:
        print("제대로 입력해주세요.")

string_format = " 당신이 입력한 수치는 {:.0f}, {:.0f} 피트입니다.\n면적은 {:.0f} 제곱 피트 {:.3f} 제곱 미터 입니다."
msg = string_format.format(height, width, height*width, height*width*0.09290304)

print(msg)

