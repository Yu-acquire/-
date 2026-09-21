m,n = input().split()
m = int(m)
conn = 0
for i in range(1,m+1,1):
    for ch in str(i):
        if ch == n:
            conn += 1
print(int(conn))
