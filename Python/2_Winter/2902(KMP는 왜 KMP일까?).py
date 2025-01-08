#입력: 최대 100글자의 영어 알파벳 대문자, 소문자, 그리고 하이픈('-', 아스키코드 45)로만 이루어져 있다.
#첫 번째 글자는 항상 대문자이다. 그리고, 하이픈 뒤에 반드시 대문자이다. 그 외의 문자는 모두 소문자이다.
#출력: 첫 줄에 짧은 형태 이름을 출력한다.
kmp = input()
results = [kmp[0]]
for char in range(len(kmp)):
    if kmp[char] == '-':
        results.append(kmp[char + 1])
print(''.join(results))