""""""
"""
연습문제 10. 셀프 계산대
간단한 셀프 계산대를 만들어 봅시다.	
총 3 개의 제품을 구매하고 제품 가격 합계, 5.5%의 세금, 총액을 출력합니다.	
각각의 물건을 구매할 때는 가격,	수량 순으로 입력받고 
3 개의 제품에 대한 정보를 모두 입력 받으면 합계, 세금,	총액 순으로 출력하면 됩니다.
입출력 예시 :
입력 화면 –
    첫번째 아이템 가격 : 25
    첫번째 아이템 수량 : 2
    두번째 아이템 가격 : 10
    두번째 아이템 수량 : 1
    세번째 아이템 가격 : 4
    세번째 아이템 수량 : 1
출력 화면 –
    중간 합계 : 64
    세금 : 3.52
    총 합계 : 67.52
"""
num_kr = ['첫', '두', '세']

item_sum = 0.0

for num_kr in num_kr:
    while True:
        item_price = input(num_kr+"번째 아이템 가격 : ")
        try:
            item_price = int(item_price)
            break
        except:
            print(num_kr+"번째 아이템의 가격을 제대로 입력해주세요.")
    while True:
        item_cnt = input(num_kr+"번째 아이템 수량 : ")
        try:
            item_cnt = int(item_cnt)
            break
        except:
            print(num_kr+"번째 아이템의 수량을 제대로 입력해주세요.")
    item_sum = item_sum + (item_price*item_cnt)

item_taxbill = (item_sum*5.5)/100
format_string = "중간 합계 : {:.0f}\n세금 : {:.2f}\n총 합계 : {:.2f}"
msg = format_string.format(item_sum, item_taxbill, item_sum+item_taxbill)

print(msg)
