""""""
"""
연습문제 5. 간단한 수학
두 개의 숫자를 입력받고,	두 숫자의 사칙연산 결과를 출력하시오.
입출력 예시 :
    입력 화면 –
    첫번째 숫자를 입력 하세요 : 10
    두번째 숫자를 입력 하세요 : 5
    출력 화면 –
    10 + 5 = 15
    10	– 5 = 5
    10	* 5 = 50
10	/ 5 = 2
"""
num1 = input('첫번째 숫자를 입력 하세요 :')
num2 = input('두번째 숫자를 입력 하세요 :')

print(num1,"+",num2,"=",int(num1)+int(num2))
print(num1,"-",num2,"=",int(num1)-int(num2))
print(num1,"*",num2,"=",int(num1)*int(num2))
print(num1,"/",num2,"=",round(int(num1)/int(num2)))

