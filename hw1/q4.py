""""""
"""
연습문제 4. Mad	Libs
명사,	동사,	형용사,	부사를 입력받아서 완성된 이야기를 출력하기!
입출력 예시 :
    입력 화면 –
    명사를 입력하세요 : dog
    동사를 입력하세요 : walk
    형용사를 입력하세요 : blue
    부사를 입력하세요 : quickly
    출력 화면 –
    Do	you	walk your blue dog	quickly? That’s hilarious!
"""
noun = input('명사를 입력하세요 :')
verb = input('동사를 입력하세요 :')
adjective = input('형용사를 입력하세요 :')
adverb = input('부사를 입력하세요 :')

print("Do you",verb,"your",adjective,noun,adverb+"?","That's hilarious!")