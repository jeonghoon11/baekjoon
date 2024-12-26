li = []
for _ in range(5):
    li.append(int(input()))
ave = sum(li) // 5
print(ave)
li.sort()
print(li[2])
