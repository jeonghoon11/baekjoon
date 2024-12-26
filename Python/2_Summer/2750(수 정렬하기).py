li = []
n = int(input())
for _ in range(n):
    li.append(int(input()))
li.sort()

for i in range(n):
    print(li[i])