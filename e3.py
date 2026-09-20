n = input()
n = float(n)
if n <= 150:
    s = n*0.4463
elif n>150 and n <= 400:
    s1 = n-150
    s=150*0.4463+s1 * 0.4663
else:
    s2 = n - 400
    s = 150*0.4463 + 250*0.4663 + s2*0.5663
print(f"{s:.1f}")