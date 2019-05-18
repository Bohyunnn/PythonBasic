""""""
"""
연습문제 2. 글자 수 세기
사용자에게 문자열을 입력받아 몇글자인지 카운트해서 출력하세요.
입출력 예시 :
    입력 화면 – String	Input	: Hello	World
    출력 화면 – Hello	World has	11	characters.
"""
# len 함수
text = input('String input: ')
cnt = len(text)
msg = text+' has '+str(cnt)+' characters.'
print(msg)

# for문
text_list = list(text)
cnt = 0
for i in text_list:
    cnt+=1
msg = text+' has '+str(cnt)+' characters.'
print(msg)