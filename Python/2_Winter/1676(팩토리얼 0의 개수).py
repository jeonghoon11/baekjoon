#문제: N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램
#입력: 첫째 줄에 N이 주어진다.(0<=N<=500)
#출력: 첫째 줄에 구한 0의 개수를 출력한다.
n = int(input())
pactorial = 1
for i in range(1, n+1):
    pactorial *= i
pactList = [int(a) for a in str(pactorial)]
counts =  0
for count in pactList[::-1]:
    if count == 0:
        counts += 1
    else:
        break

print(counts)