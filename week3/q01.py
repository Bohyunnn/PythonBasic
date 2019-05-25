# 5명의 수학 성적을 입력받아서
# 평균과 총 합을 구하시오

score_list = range(1,5)
total_score = 0
avg_score = 0

# 숫자로 제대로 입력할 때까지 계속 반봅
for i in range(1,6) :
    while True:
        score = input("수학성적을 입력하세요 : ")
        try:
            score = int(score)
            total_score += score
            # 제대로 입력이 완료 되었다면 반복문을 종료한다.
            break
        except:
            print("제대로 입력해 주세요.")
avg_score = total_score/5
print("점수합계 = ", total_score, "점수 평균 = ", avg_score)