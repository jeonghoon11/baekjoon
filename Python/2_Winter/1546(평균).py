#입력한 점수 중 최대값을 M이라 하고 모든 점수를 점수/M*100으로 고쳤다.
#입력: 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 둘째 줄에 성적이 주어진다.
#출력: 첫째 줄에 새로운 평균을 출력한다.
n = int(input())
arr = list(map(int, input().split()))
maxScore = max(arr)
for i in range(len(arr)):
    arr[i] = arr[i]/maxScore*100

print(sum(arr)/n)