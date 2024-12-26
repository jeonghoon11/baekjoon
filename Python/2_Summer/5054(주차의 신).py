n = int(input())

for i in range(n):
    shop = int(input())
    li = list(map(int, input().strip().split()))
    print((max(li)-min(li))*2)
