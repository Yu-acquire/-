n = int(input())
zid = {}
lst = []
for _ in range(n):
    name,a,b,c=input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    t = a + b + c
    zid[name] = [a,b,c,t]
    lst.append(name)
for i in range(n):
    for j in range(i+1,n):
        n1 = lst[i]
        n2 = lst[j]
        a1,b1,c1,t1 = zid[n1]
        a2,b2,c2,t2 = zid[n2]
        if abs(a1 - a2) <=5 and abs(b1 - b2) <=5 and abs(c1 - c2) <=5 and abs(t1 - t2) <=10:
            print(f"{n1} {n2}")