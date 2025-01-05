#입력: 첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다.
#S의 길이는 100을 넘지 않는다.
#출력: 첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.
inp = list(input())
result = []
for char in inp:
    if 'A' <= char <= 'Z':
        if 'Z' < chr(ord(char) + 13):
            result.append(chr(ord(char) - 13))
            continue
        result.append(chr((ord(char) + 13)))
    elif 'a' <= char <= 'z':
        if 'z' < chr(ord(char) + 13):
            result.append(chr(ord(char) - 13))
            continue
        result.append(chr((ord(char) + 13)))
    else:
        result.append(char)

print("".join(map(str , result)))