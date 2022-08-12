import math
a = float(input())
area = round(2 * math.sqrt(3) * pow(a, 2), 2)
volume = round(1 / 3 * math.sqrt(2) * pow(a, 3), 2)

octahedron = [str(area), str(volume)]

print(" ".join(octahedron))
