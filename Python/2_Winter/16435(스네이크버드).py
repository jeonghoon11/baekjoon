n, l = map(int, input().split())
arr = list(map(int, input().split()))    
cnt = l

arr = sorted(arr)

for num in arr:
    if num <= cnt:
        cnt += 1
    else:
        break

print(cnt)