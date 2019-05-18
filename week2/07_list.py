""""""
"""
바구니 객체 - range()
바구니 객체 - 시퀀스 객체(문자열, 리스트), 딕셔너리, 튜플, 셋
 1) 만들기
 2) 값 꺼내기
 3) 값 변경하기
 4) 값 추가하기
 5) 값 삭제하기
"""

#  리스트
test_list = [] # 비어있는 리스트
# test_list = list()
test_list = [1,2,3,4,5]
# test_list = [1, "a", 3.14 ,"hello"]
# 바구니 변수에는 여러 종류의 값들을 여러 개 저장할 수 있다.
print(test_list[0])
test_list[0] = 7
print(test_list[0]) # 인덱스로 접근해서 리스트의 값 변경 가능하다.

# append(object)
test_list.append(99)
test_list.append(99)
test_list.append(99)
print(test_list)

# insert(index, object)
test_list.insert(-3, 98)     # 없는 위치에 넣으면 마지막 값에 붙음, -는 뒤에서 부터 셈.
print(test_list)

# remove는 같은 값이 있으면 맨 앞에 값만 지움.
if 123134 in test_list:
    test_list.remove(123134)
    print(test_list)
    print('if문으로 지움')

if test_list.__contains__(99):
    test_list.remove(99)
    print(test_list)

# pop()
number = test_list.pop()
print(number)
number = test_list.pop(2)
print(number)
print(test_list)




