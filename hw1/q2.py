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