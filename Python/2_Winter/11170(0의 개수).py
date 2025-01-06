#입력: 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#     각 줄에 N과 M이 주어진다.
#출력: 각각의 테스트 케이스마다 N부터 M까지의 0의 개수를 출력한다.
t = int(input())
result = []
for _ in range(t):
    counts = 0
    n, m = map(int, input().split())
    for num in range(n,m+1):
        numL = [int(a) for a in str(num)]
        for count in numL:
            if count == 0:
                counts += 1
    result.append(counts)

for i in range(t):
    print(result[i])