#피보나치 수는 0과 1로 시작한다.
#입력: 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
#출력: 첫째 줄에 n번째 피보나치 수를 출력한다.
n = int(input())
arr = [0, 1]
for i in range(n-1):
    arr.append(arr[i]+arr[i+1])

print(arr[n])