"""
"""
"""
format 명령어를 이용한 format_string
돈! 12,345,678
"""
balance = 12341234
interest = 5
number_of_count = 4
number_of_years = 10
final_balance = balance*(1+interest/100/number_of_count)**(number_of_count*number_of_years)

"""
.format 옵션
{}: 자리 만들기
{0} : index를 써주면 입력된 값들 중 해당 위치의 값이 출력된다.
{ :s} : 입력된 값의 타입을 지정하려면 :(콜론)을 찍고 그 뒤에 양식을 지정한다.
{0:f}
{:2f}: 양식 문자 앞에 숫자를 써서 자릿수를 제한할 수 있다.
< : 왼쪽 정렬
> : 오른쪽 정렬
^ : 가운데 정렬
{:,d} : ,(콤마)를 사용하면 통화 단위처럼 표시할 수 있다.  
"""

format_string = "원금이 {:>10,d}원, 연이율 {:^10.2f}%, 연지급회수 {:d}회인 예금에 {:d}년 동안 예금을 해두면 최종 원리금은 {:,.2f}원입니다."
msg_string = format_string.format(balance, interest, number_of_count, number_of_years, final_balance)

print(msg_string)