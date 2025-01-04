k = int(input())
result = []
gap = [0] * k
for i in range(k):
    line = list(map(int, input().split()))
    studentCount = line[0]
    scores = sorted(line[1:], reverse=True)
    result.append(scores)
    for j in range(len(scores) - 1):
        if scores[j] - scores[j+1] > gap[i]:
            gap[i] = scores[j] - scores[j+1]
for i in range(k):
    print(f"Class {i+1}")
    print(f"Max {max(result[i])}, Min {min(result[i])}, Largest gap {gap[i]}")