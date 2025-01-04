#입력: T개의 테스트 데이터로 구성. 첫 번쨰 줄에는 입력 데이터의 수를 나타내는 정수 T
#각 테스트 데이터는 한 줄로 구성. 7개의 자연수가 공백으로 구분되어 있다. 7개의
#자연수 중 적어도 하나는 짝수
#출력: 각 테스트 데이터에 대해, 7개 자연수 중 짝수의 합과 최솟값을 공백으로 구분하여 하나씩 출력.
#results 리스트를 튜플 구조로 생성. 이후 언패킹
t = int(input())
results = []
for i in range(t):
    line = list(map(int, input().split()))
    evens = [num for num in line if num % 2 == 0]
    results.append((sum(evens), min(evens)))

for i in range(t):
    print(*results[i])