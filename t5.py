n = int(input())
goods = []
for _ in range(3):
    a,b = map(int, input().split())
    goods.append( (a,b) )

res = []
for k, v in goods:
    pack = n // k
    if n % k != 0:
        pack += 1
    cost = pack * v
    res.append(cost)
print(min(res))