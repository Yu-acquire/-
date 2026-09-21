num = list(map(int,input().split()))
num.sort()
hasm = {'A':num[0],'B':num[1],'C':num[2]}
order = input().strip()
res = [hasm[c] for c in order]
print(' '.join(map(str,res)))