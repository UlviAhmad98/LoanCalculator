import math
x = abs(int(input()))
y = int(input())

if y <= 1:
    print(round(math.log(x), 2))
else:
    print(round(math.log(x, y), 2))
