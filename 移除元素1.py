nums = list(map(int,input().split()))
n = int(input())

i,j = 0,0
for j in range(len(nums)):
    if nums[j] != n:
        nums[i] = nums[j]
        i += 1
print(i)
print(nums[:i])
print(' '.join(map(str,nums[:i])))

