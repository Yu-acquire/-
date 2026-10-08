class Solution:
    def removeword(self,nums:list[int],vel:int)-> int:
        fast,slow = 0,0
        size = len(nums)
        while fast < size:
            if nums[fast] != vel:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(nums[:slow])
        return slow
objs = Solution()
nums = list(map(int,input().split()))
vel = int(input())
obj = objs.removeword(nums,vel)
print(obj)
