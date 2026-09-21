def fact(n):
    s = 0
    for m in range(n,0,-1):
        t = 1
        for i in range(1,m+1):
            t = t*i
        s=s+t
    return s

a = int(input())
n = fact(a)
print(int(n))