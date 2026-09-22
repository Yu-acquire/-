w, x, h = map(int, input().split())
q = int(input())
removed = [[[False]*(h+2) for _ in range(x+2)] for __ in range(w+2)]
for _ in range(q):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            for k in range(z1, z2+1):
                removed[i][j][k] = True
cnt = 0
for i in range(1, w+1):
    for j in range(1, x+1):
        for k in range(1, h+1):
            if removed[i][j][k]:
                cnt += 1
total = w * x * h
ans = total - cnt
print(ans)