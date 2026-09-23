def zhishu(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
ans = []
for num in a:
    if zhishu(num):
        ans.append(str(num))
print(' '.join(ans))