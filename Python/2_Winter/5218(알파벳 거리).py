#입력: 첫째 줄에 테스트 케이스의 수가 주어진다.
#각 테스트 케이스는 한 줄로 이루어져 있고, 두 단어가 공백으로 구분되어져 있다.
#출력: 각 테스트 케이스 마다 각 글자의 알파벳 거리를 공백으로 구분해 출력한다.
n = int(input())
result = []
for _ in range(n):
    first, second = map(str, input().split())
    line = []
    for i in range(len(first)):
        if ord(second[i]) - ord(first[i]) < 0:
            line.append(ord(second[i]) + 26 - ord(first[i]))
        else:
            line.append(ord(second[i]) - ord(first[i]))
    result.append(line)

for num in result:
    print(f'Distances: {' '.join(map(str, num))}')