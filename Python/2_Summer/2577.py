a = int(input())
b = int(input())
c = int(input())

abc = a * b * c
number = list(map(int, str(abc)))
in_dex = [0] * 10
for i in range(len(number)):
    for j in range(10):
        if number[i] == j:
            in_dex[j] += 1

for count in in_dex:
    print(count)