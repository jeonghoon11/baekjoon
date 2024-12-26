for _ in range(int(input())):
    n, in_put = input().split()
    n = int(n)
    print(in_put[:n-1],in_put[n:], sep=(''))