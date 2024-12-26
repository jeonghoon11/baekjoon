li = []
for _ in range(8):
    li.append(int(input()))

li_copy = li
li.sort(reverse=True)   #큰 수 부터

print(sum(li[:5]))  #큰수 5개 합

# li_copy.index()

li_average = sum(li) // 8

for i in range(8):
    if li_copy[i] > li_average:
        print(i + 1, end = ' ')

'''first = li_copy[0]
first_index = 0

for i in range(8):
    if li_copy[i] < li_average:
        if li_copy[i] > first_index:
            first_index = li_copy[i].index()
print(first.index())'''