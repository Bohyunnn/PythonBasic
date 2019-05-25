""""""
"""
바구니 객체: 한 변수(저장공간)에 여러가지의 값을 여러개 한꺼번에 저장해 두는 역할
종류: 리스트, 딕셔너리, 튜플, 셋
바구니를 다루는 기법
1. 하나씩 꺼내서 다루는 법 - for
2. 원하는 요소를 선택해서 다루는 법: 인덱스 + 슬라이싱
"""
# * 빈 리스트는 if문에서 False가 나온다
test_list = list()
test_list = []
"""
- 리스트에 요소가 있으면 처리를 하겠다.
if test_list:
    pass  
- 리스트에 요소가 없으면 처리를 하겠다.
if not test_list:
    pass
"""
# number = input()
# test_list.append(number)
# 변수에 처음으로 값을 할당하는 행위를 초기화
test_list = [1,2,3,4,5,6]

# 만약 1~10000까지 담겨있는 리스트를 만들어라
for number in range(1,10001) :
    test_list.append(number)

# test_list에는 range(1,10001) 형태 그대로 들어감
test_list = range(1,10001)
# range를 list로 형변환
test_list = list(range(1,10001))

#index는 0부터 시작
# 리스트에서 값을 하나 꺼내려면 index를 사용한다.
test_list[3]
test_list[3] = 7
test_list.remove(값)
# 만약 동일한 값이 여러 개인 경우, 처음에 나온 1개만 삭제된다.
# 만약 없는 값을 삭제하려하면 오류가 발생한다.
test_list.remove(100)

# 값이 있는지 없는지 체크
if 100 in test_list:
    test_list.remove(100)
# 맨 마지막 값을 꺼낸다.
test_list.pop()
# 해당 위치에 있는 값을 꺼낸다.
test_list.pop(인덱스)

# 값을 추가하는 방법
# append
# insert

# 값을 맨 끝에 추가한다.
test_list.append(값)
# 해당 값을 해당 위치에 추가한다.
test_list.insert(index, 값)

# 만약 해당하는 index가 없는 경우에는 맨 끝 혹은 맨 앞에 추가된다.




