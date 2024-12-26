for _ in range(int(input())):
    li = []
    n = bin(int(input()))[2:][::-1]

    for i in range(len(n)):
        if n[i] == '1':
           li.append(i)

    for i in li:
        print(i, end=' ')  #한 칸 띄워서 출력