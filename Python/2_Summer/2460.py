s_passengers = []

out, i_n = map(int, input("내린 사람, 탄 사람 입력: ").split())
s_passengers.append(i_n)

for i in range(1, 10):
    out, i_n = map(int, input("내린 사람, 탄 사람 입력: ").split())
    s_passengers.append(s_passengers[i-1] - out + i_n)

max_passengers = s_passengers[0]

for i in range(1, 10):
    if s_passengers[i] > max_passengers:
        max_passengers = s_passengers[i]

print(max_passengers)