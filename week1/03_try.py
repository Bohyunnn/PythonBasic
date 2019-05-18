# 오류 구문 처리 try - catch
number = input('정수만 입력하세요: ')
try:
    number = int(number)
    print(number*2)
    # 오류가 날지도 모르는 코드
except:
    # 아무것도 실행 안하고 넘어갈때는 pass
    # except 오류 설정할 수 있음
    print('숫자만 입력할 수 있습니다.')
