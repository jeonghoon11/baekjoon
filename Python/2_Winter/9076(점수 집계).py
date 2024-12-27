#입력: 테스트 케이스의 개수 입력 후 각 테스트 케이스는 한 줄에 다섯개씩 공백을 사이에 두고 입력
#출력: 최고점과 최저점을 뺀 나머지 3명 점수의 최고점과 최저점의 차이가 4점 이상 나게 되면
#KIN출력, 4점 이상 차이가 나지 않으면 최고점과 최저점을 뺀 값들의 합을 출력.
arr = []
a = int(input())

for i in range(a):
    line = list(map(int, input().split()))
    arr.append(line)

for i in range(a):
    arr[i].sort(reverse=False)
    if (arr[i][3] - arr[i][1]) >= 4:
        print("KIN")
    else:
        result = 0
        for j in range(3):
            result += arr[i][j+1]
        print(result)