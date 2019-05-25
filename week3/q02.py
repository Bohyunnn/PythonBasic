# 5명의 수학 성적을 입력받아서
# 평균과 총 합을 구하시오
# 5명이 아니라 입력값이 있는 동안 계속 성정 입력하기(반복문 조건 설정)
# 최대 최솟값 찾기( 최대, 최소값을 찾으면서 진행 / 모든 값을 저장해 둔 다음에 정렬해서 찾기)
total_score = 0
avg_score = 0
person_num = 0
score_max =0
score_min =0

# 숫자로 제대로 입력할 때까지 계속 반복
while True:
    print("=== MENU를 선택해주세요===")
    print("1. 값 입력 받기")
    print("2. 합계와 평균 출력하기")
    print("3. 최대값과 최소값 출력하기")
    print("4. 프로그램 종료하기")
    menu = input("메뉴를 선택해주세요 : ")

    if menu == "1":
        while True:
            score = input("수학성적을 입력하세요 : ")
            try:
                score = int(score)
                total_score += score
                if score > score_max:
                    score_max = score
                if score_min == 0:
                    score_min = score
                elif score < score_min:
                    score_min = score
                person_num += 1
                break
                # 제대로 입력이 완료 되었다면 반복문을 종료한다.
            except:
               print("제대로 입력해주세요.")
        avg_score = total_score/person_num
    elif menu == "2":
        print(person_num, "점수합계 = ", total_score, "점수 평균 = ", avg_score)
    elif menu == "3":
        print("최대점수 = ",score_max, "최소점수 =",score_min)
    else :
        break