class Solution:
    def move(self,nums:list[int]):
        fast,slow = 0,0
        size = int(len(nums))
        l = size - 1
        while fast < size:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast +=1
        while slow < size:
            nums[slow] = 0
            slow += 1
        return nums
obj = Solution()
objs = obj.move(list(map(int,input().split())))
print(objs)