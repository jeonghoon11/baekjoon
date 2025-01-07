#입력: 첫째 줄에 자연수S가 주어진다.
#출력: 첫째 줄에 자연수 N의 최댓값을 출력한다.
s = int(input())
count = 0
while True:
    s = s - count
    if s< 0:
        count -= 1
        break
    else:
        count += 1

print(count)