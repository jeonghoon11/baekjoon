arr = []
count = 0
for _ in range(10):
    arr.append(int(input()) % 42)

for i in range(42):
    for j in range(10):
        if arr[j] == i:
            count += 1
            break

print(count)