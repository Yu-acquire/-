cnt = [0] * 10
M, N = map(int, input().split())
for num in range(M, N + 1):
    x = num
    while x > 0:
        d = x % 10
        cnt[d] += 1
        x = x // 10
print(' '.join(map(str, cnt)))


cnt = [0] * 10
M, N = map(int, input().split())
for num in range(M, N+1):
    for c in str(num):
        d = int(c)
        cnt[d] += 1
print(' '.join(map(str, cnt)))


M, N = map(int, input().split())
s = ''.join(str(i) for i in range(M, N+1))
cnt = [s.count(str(d)) for d in range(10)]
print(' '.join(map(str, cnt)))