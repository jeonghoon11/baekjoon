li = [int(input()) for _ in range(9)]
total_sum = sum(li)

for i in range(9):
    for j in range(i + 1, 9):
        if total_sum - li[i] - li[j] == 100:
            result = [li[k] for k in range(9) if k != i and k != j]
            result.sort()
            break
    else:
        continue
    break

for li in result:
    print(li)