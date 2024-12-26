#입력: 10개의 자연수
#출력: 첫째 줄에는 평균 출력, 둘째 줄에는 최빈값을 출력.
#최빈값이 둘 이상일 때에는 그 중 하나만 출력.
arr = []
value = [0, 0]
temp = [0, 0]

for i in range(10):
    arr.append(int(input()))

for i in range(10):
    temp[0] = arr[i]
    temp[1] = 0
    for j in range(i, len(arr)):
        if temp[0] == arr[j]:
            temp[1] += 1
    if temp[1] > value[1]:
        value[0] = temp[0]
        value[1] = temp[1]

print(sum(arr)//len(arr))
print(value[0])