#입력: 첫 줄에 테스트 케이스의 개수 T가 주어진다.
#출력: 콤마로 이루어진 입력의 합을 출력
t = int(input())  # 테스트 케이스 개수 입력

for _ in range(t):
    a, b = map(int, input().split(','))
    print(a + b)