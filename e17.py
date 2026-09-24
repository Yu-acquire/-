m,n = map(int,input().split())
res = input().split()
nums = []
t = 0
for i in res:
    if i in nums:
        t = t
    else:
        nums.append(i)
        t += 1
    if len(nums)>m:
        del nums[0]
print(t)