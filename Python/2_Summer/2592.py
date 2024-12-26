import numpy as np
import statistics as st

number = []
for i in range(10):
    number.append(int(input()))

average = np.mean(number)

#근데도 런타임 에러뜨네요.??
try:
    ch = st.mode(number)    #이것만 해도 값은 잘 나오는데 백준에서 런타임오류나서 쥐선생님 도움
except st.StatisticsError as e:
    ch = "No unique mode found"

print(int(average))
print(ch)