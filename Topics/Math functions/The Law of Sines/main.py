# put your code here
import math

B_deg = 35
C_deg = 105
A = 40
b = 7
B = math.radians(B_deg)
C = math.radians(C_deg)
c = b * math.sin(C) / math.sin(B)

print(round(c, 1))