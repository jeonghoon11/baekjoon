n = int(input())
people = []

for _ in range(n):
    name, dd, mm, year = input().split()
    people.append((name, int(year), int(mm), int(dd)))

people.sort(key=lambda x: (x[1], x[2], x[3]))

print(people[-1][0])
print(people[0][0])