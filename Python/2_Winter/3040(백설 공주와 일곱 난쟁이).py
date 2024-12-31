#문제: 아홉 개의 정수를 입력받고 합이 100이 되는 숫자조합 출력.
#입력: 총 아홉개 줄에 9개의 숫자 입력 단, 모든 숫자는 서로 다르다.
#출력: 한 줄에 하나씩 출력.
arr = []
for _ in range(9):
    arr.append(int(input()))
total = sum(arr)
for i in range(9):
    for j in range(i+1, 9):
        if total - (arr[i] + arr[j]) == 100:
            removeI, removeJ = arr[i], arr[j]
            break

for num in arr:
    if num != removeI and num != removeJ:
        print(num)