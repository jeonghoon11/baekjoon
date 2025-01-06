#입력: 첫째 줄에 N과 K가 주어진다. 둘째 줄부터 N개의 줄에 동전의 가치 A가 오른차순으로 주어진다.
#출력: 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
#그리디 알고리즘
n, k = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
money.sort(reverse=True)

count = 0
for coin in money:
    if k == 0:
        break
    count += k // coin
    k %= coin

print(count)