#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지
#알아내는 프로그램을 작성. 단, 대소문자 구분X
#입력: 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
#출력: 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
#단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

n = input().upper()
arr = [0] * 26

for char in n:
    if 'A' <= char <= 'Z':
        idx = ord(char) - 65
        arr[idx] += 1

maxCount = max(arr)
if arr.count(maxCount) > 1:
    print('?')
else:
    print(chr(65 + arr.index(maxCount)))