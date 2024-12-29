#입력: 첫 번째 줄에 정수 K가 주어진다.
#이후 K개의 줄에 정수가 1개씩 주어진다. 정수가 "0"일 경우네느 가장 최근에 쓴 수를 지우고,
#아닐 경우 해당 수를 쓴다.
#출력: 받아 적은 수의 합
k = int(input())
stack = []

for _ in range(k):
    num = int(input())
    if num == 0:
        if stack:
            stack.pop()
    else:
        stack.append(num)
print(sum(stack))