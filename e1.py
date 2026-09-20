import math

s = input().split()
a = float(s[0])
b = float(s[1])
c = float(s[2])
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"{s:.1f}")