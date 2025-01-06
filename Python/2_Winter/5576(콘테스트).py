#입력: 1번째 줄부터 10번째 줄에는 W대학의 각 참가자의 점수를 나타내는 정수
# 11번째 줄부터 20번째 줄에는 K 대학의 각 참가자의 점수를 나타내는 점수.
#출력: W대학 점수와 K대학의 점수를 순서대로 공백으로 구분하여 출력.
w = []
k = []
for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))
w.sort(reverse=True)
k.sort(reverse=True)
wResult = sum(w[:3])
kResult = sum(k[:3])
print(wResult, kResult)