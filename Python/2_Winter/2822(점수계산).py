#8개의 입력값을 받고 첫번째 출력에 가장 큰 값 5개의 합을 출력.
#두번째 출력줄에 높은 값 5개의 index값 출력. 예) 3 4 5 6 8 

arr1 = []
for i in range(8):
    arr1.append(int(input()))

arr2 = list(arr1)
arr2.sort(reverse=True)
arr2 = arr2[0:5]
#arr2 = sorted(arr1, reverse=True)[:5]

arr3 = []
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr2[j] == arr1[i]:
            arr3.append(i+1)

result1 = sum(arr2)
print(result1)
# print(arr3)
print(" ".join(map(str, arr3)))