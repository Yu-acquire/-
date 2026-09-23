n,m = map(int,input().split())
lst = []
res = []
idx = 0
for i in range(1,n+1):
    lst.append(i)

while lst:
    idx = (idx + m -1) % len(lst)
    out = lst.pop(idx)
    res.append(out)

print(' '.join(map(str,res)))