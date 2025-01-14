results = []
while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break

    if a + b <= c or a + c <= b or b + c <= a:
        results.append("Invalid")
    elif a == b == c:
        results.append("Equilateral")
    elif a == b or b == c or a == c:
        results.append("Isosceles")
    else:
        results.append("Scalene")

for result in results:
    print(result)