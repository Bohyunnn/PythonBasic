"""
판별문
if문은 판별문이다.
if문을 구성하는 판별문은 if, elif, else
if : 만약 조건문1이 참이라면 해당 실행구문들1을 실행한다.(1)
elif: 그게 아니라 만약 조건문2가 참이라면 실행구문들2을 실행한다. (0~)
else: 위에 조건이 전부 다 아니라면 실행구문들3을 실행한다. (0,1)
if  [조건문1] :
    [실행구문들1]
elif [조건문2] :
    [실행구문들2]
else :
    [실행구문들3]
"""

num = 3

if num > 5:
    print("숫자가 5보다 큽니다.")
elif num == 5:
    print("숫자가 5 입니다.")
else:
    print("숫자가 5보다 크지 않습니다.")

"""
조건식이 뭐야?
조건식의 명제 -> 참과 거짓을 판별할 수 있는 문장
조건식은 결과가 Boolean 값(boole)이 나오는 것 => True, False

1) 비교 연산자
== 같다. 
!= 같지 않다. 
> 크다.
< 작다.
>= 크거나 같다.
<= 작거나 같다. 

2) 값에 대해서 
숫자 : 0은 False, 나머지는 모두 True
문자 : ''은 False, 나머지는 모두 False
bool : False, True
None : False
리스트나 딕셔너리 : [], {}(빈값인 경우) False, 나머지는 True
[[]] : {공집합} True
"""
"""
AND, OR, NOT
and : (a>b and b>c)
or : (a>b or b>c)
not : a=0 조건의 반전
if not a : # a가 만약에 비어있다면
    pass
"""