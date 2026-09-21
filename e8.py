n = int(input())
lst1 = list(map(int,input().split()))
lst2 = []
for i in range(0,n):
    lst2.append(lst1[i])
max_num = max(lst2)
min_num = min(lst2)
m = max_num - min_num
print(m)