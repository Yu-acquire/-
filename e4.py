s1 = list(input().strip())
s2 = list(input().strip())
s1 = s1[::-1]
s2 = s2[::-1]
carr = 0
res = []
max_len = max(len(s1), len(s2))

for i in range(max_len):
    if i < len(s1):
        num1 = int(s1[i])
    else:
        num1 = 0

    if i < len(s2):
        num2 = int(s2[i])
    else:
        num2 = 0

    total = num1 + num2 + carr
    res.append(str(total % 10))
    carr = total // 10

if carr != 0:
    res.append(str(carr))
ans = res[::-1]
print(''.join(ans))