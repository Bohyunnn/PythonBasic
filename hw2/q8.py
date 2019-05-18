""""""
"""
연습문제 8. 피자 파티
피자를 정확하게 나누는 프로그램을 작성하세요.	
사람 수,피자 개수,조각 개수를 입력받습니다.	이때 조각 개수는 짝수여야 합니다.	
한 사람이 받게 되는 피자 조각 개수를 출력하고, 남는 피자 개수도 출력하시오.
입출력 예시 :
입력 화면 –
    인원수를 입력하세요 : 8
    피자 수를 입력하세요 : 2
    한 피자당 조각 개수를 입력하세요 : 8
출력 화면 –
    8 명이서 피자 2 개를 먹을 때
    한명당 2 조각의 피자를 먹을 수 있습니다.
    남는 조각은 0 개 입니다.
추가 내용 :
    모든 입력은 숫자만 입력되어야 합니다.	숫자가 아닌 글자가 입력되면 다시 입력받도록
    해보세요.
"""

while True:
    member_cnt = input("인원수를 입력하세요. : ")
    try:
        member_cnt = int(member_cnt)
        break
    except:
        print("인원수를 제대로 입력해주세요.")

while True:
    pizza_cnt = input("피자수을 입력하세요. : ")
    try:
        pizza_cnt = int(pizza_cnt)
        break
    except:
        print("피자수를 제대로 입력해주세요.")

while True:
    pizza_piece_cnt = input("한 피자당 조각 개수를 입력하세요. : ")
    try:
        pizza_piece_cnt = int(pizza_piece_cnt)
        if pizza_piece_cnt % 2 == 0:
            break
        else:
            print("한 피자당 조각 개수는 짝수여야 합니다.")
    except:
        print("한 피자당 조각 개수를 제대로 입력해주세요.")

string_format = "{:d} 명이서 피자 {:d} 개를 먹을 때 \n한명당 {:.0f} 조각의 피자를 먹을 수 있습니다.\n남는 조각은 {:d} 개 입니다."
total_pizza_piece = pizza_cnt*pizza_piece_cnt
member_pizza_piece = total_pizza_piece/member_cnt
leave_pizza_piece = total_pizza_piece%member_cnt

msg = string_format.format(member_cnt, pizza_cnt, member_pizza_piece, leave_pizza_piece)

print(msg)