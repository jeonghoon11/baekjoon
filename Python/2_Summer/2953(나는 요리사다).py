a,b,c,d = map(int, input().split())
max = a+b+c+d
n = 1
for i in range(4):
    a, b, c, d = map(int, input().split())
    sum = a+b+c+d
    if sum > max:
        max = sum
        n = i + 2
print(n,max)