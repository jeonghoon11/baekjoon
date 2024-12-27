#배열 A가 주어졌을 때, N번째 큰 값을 출력.
#배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.
#입력: 테스트 케이스 개수(한 줄로 공백으로 입력받음)
#출력: 각 테스트 케이스에 대해 한 줄에 하나씩 배열 A에서 3번쨰 큰 값을 출력.
arr = []
a = int(input())

for i in range(a):
    line = list(map(int, input().split()))
    arr.append(line)

for i in range(a):
    print(sorted(arr[i], reverse=True)[2])