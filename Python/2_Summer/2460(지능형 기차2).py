n, k = map(int, input().split())
result = maxIn = k - n
for _ in range(9):
    n, k = map(int, input().split())
    result = k - n + result
    if result > maxIn:
        maxIn = result

print(maxIn)