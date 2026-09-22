M,N = map(int,input().split())
r = 0
cnt = []
for n in range(M,N+1):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        r += 1
        cnt.append(n)
print(f"{r}\n{' '.join(map(str,cnt))}")