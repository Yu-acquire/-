
class Solution:
    def  twoSum(self,nums:list[int],target:int):
        hashmap =  {}
        for idx,num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement],idx]
            else:
                hashmap[num] = idx

        return []

obj = Solution()
res = obj.twoSum([3,2,4],  7)
print(res)