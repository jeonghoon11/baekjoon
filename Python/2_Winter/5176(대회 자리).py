#입력: 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
#첫째 줄에 참가자의 수 P와 자리의 수 M이 주어진다.
#다음 P개 줄에는 각 참가자가 원하는 자리가 주어진다.
#자리는 1번부터 M번까지 있다. 입력으로 주어지는 참가자가 도착하는 순서이다.
#출력: 각 테스트 케이스에 대해서, 대회에 참가하지 못하는 사람의 수를 출력한다.
s = []
k = int(input())
for _ in range(k):
    p, m = map(int, input().split())
    line = []
    result = 0

    for j in range(p):
        lineInput = int(input())
        if lineInput <= m:
            if lineInput not in line:
                line.append(lineInput)
            else:
                result += 1
        else:
            result += 1

    s.append(result)

for res in s:
    print(res)