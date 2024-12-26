c = []
for i in range(100):
    c.extend([i] * i)   #한번에 여러개를 리스트에 추가

a, b = map(int, input().split())

result = sum(c[a-1:b])
print(result)