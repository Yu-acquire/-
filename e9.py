lst1 = list(map(int,input().split()))
lst2 = []
for i in range(0,len(lst1)+2):
    if lst1[i] == 0:
        break
    lst2.append(lst1[i])
lst2.reverse()
print(' '.join(map(str, lst2)))
