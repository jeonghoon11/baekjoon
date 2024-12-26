#strip은 공백문자를 지울 수 있다. (lstrip , rstrip 등..)
n = int(input()) #리스트의 크기는 입력받아야 하지만, 파이썬에서는 리스트의 크기와 관계없이 리스트를 처리할 수 있기 때문에
                 # n은 코드에서 실제로 사용되지 않습니다.

li = list(map(int, input().strip().split()))
count = 0

result = int(input())

count = li.count(result)

print(count)

''' 처음 코드
li = []
count = 0
for _ in range(int(input())):
    li.append(int(input()))

result = int(input())

for i in range(len(li)):
    if li[i] == result:
        count += 1

print(count)
'''