#입력: 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
#출력: 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ...z가 처음 등장하는 위치를
#공백으로 구분해서 출력한다. 만약 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력. 단어의 첫 번째
#글자는 0번째 위치, 두 번째 글자는 1번째 위치이다.

#python에서 아스키 값은 chr(값)으로 나타냄 a=97, z=122 ord(a)는 반대로 97로 나타남.
#join함수는 문자열을 연결. arr이 정수형이므로 map으로 전체를 string으로 변환
s = input()
arr = [-1] * 26

for i in range(len(s)):
    idx = ord(s[i]) - 97
    if arr[idx] == -1:
        arr[idx] = i
print(" ".join(map(str, arr)))