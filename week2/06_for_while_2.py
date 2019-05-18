""""""
"""
반복문은 같은 여러번 반복하여 입력하는 것이 비효율적이기 때문에
같은 코드를 반복실행 할 때 사용하는 것
while ~ 동안
for 몇회
break: 만나는 즉시 break를 감싸고 있는 가장 가까운 반복문을 종료
continue: 만나는 즉시 그 이하의 구문은 실행하지 않고 반복문의 다음 회차로 이동
"""
"""
number = 0
while number <= 10:
    number = number + 1
    if number % 2 == 0:
        continue
    print(number)

number = 0
while number <= 10:
    number = number + 1
    if number % 2 != 0:
        print(number)
"""
# for [바구니에서 꺼낸 요소의 이름] in [바구니]
#       [실행구문들]
# range : 범위 생성자
# range(y) : 0부터 (y-1)까지의 범위
# range(x,y) : x부터 (y-1)까지의 범위
# range(x,y,z): x부터 (y-1)까지의 범위, z만큼 증감치

# 1에서 100까지의 합
total = 0
for number in range(1,101) :
    total = total + number
print(total)

# 1에서 100까지의 홀수들의 합
even_total = 0
for number in range(1,101): # for number in range(2,101,2):
    if number % 2 ==0:
        even_total = even_total + number
print(even_total)

odd_total = 0
for number in range(1,101): # for number in range(1,101,2):
    if number % 2 !=0:
        odd_total = odd_total + number
print(odd_total)

msg ="Hello World"
# len 바구니 형태에는 다 사용가능
print(len(msg))
cnt = 0
for char in msg:
    cnt = cnt + 1
print(cnt)

# 바구니 객체 - index가 있는 변수
# 인덱싱 : 해당 순번을 지정해서 위치에 있는 값만 꺼내보기 (하나만, 0부터 시작)
# 슬라이싱 : x번부터 y번까지 일부만 꺼내보기 (하나이상)
# 변수[번호:] : 시작 번호
# 변수[:번호] : 끝 번호
# 변수[::번호]
msg ="Hello World"
print(msg)
print(msg[4])
print(msg[-2])
print(msg[3:])
print(msg[:5])
print(msg[::2])
print(msg[::-1])

