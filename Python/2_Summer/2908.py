a, b = map(int, input().split())

a1 = (a//100) + ((a//10 - (a//100) * 10))*10 + (a % 10) * 100
b1 = (b//100) + ((b//10 - (b//100) * 10))*10 + (b % 10) * 100

if a1 < b1:
    print(b1)
else:
    print(a1)
'''
a1 = a[::-1]
b1 = b[::-1]

print(a1, b1)
'''