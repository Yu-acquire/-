def f(x,a,b,c,d):
    return (a*x**3)+(b*x**2)+(c*x)+d
res = []
a,b,c,d= map(float,input().split())

for i in range(-100,100):
    l = i
    r = i+1
    if f(r,a,b,c,d) ==0:
        res.append(r)
        continue
    if f(l,a,b,c,d)*f(r,a,b,c,d)<0:
        for _ in range(100):
            mid = (l+r)/2
            if f(mid,a,b,c,d) * f(l,a,b,c,d)<0:
                r = mid
            else:
                l = mid
        res.append((l+r)/2)
        if len(res) == 3:
            break
print(f'{res[0]:.2f} {res[1]:.2f} {res[2]:.2f}')




