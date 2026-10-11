class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i,j = 0,0
        sums = 0
        min_l = float('inf')
        l = len(nums)
        for j in range(l):
            sums += nums[j]
            while sums >= target:
                min_l = min(min_l,j - i +1)
                sums -= nums[i]
                i += 1
        if min_l == float('inf'):
            min_l = 0
        return min_l

obj = Solution()
objs = obj.minSubArrayLen( 11, [1,1,1,1,1,1,1,1])
print(objs)

