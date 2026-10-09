class Pingf:
    def ping(self,nums:list[int]) -> int:
        rels = []

        i = 0
        j = len(nums) - 1
        while i <= j:
            a = nums[i] * nums[i]
            b = nums[j] * nums[j]
            if a > b:
                rels.append(a)
                i += 1
            else:
                rels.append(b)
                j -= 1
        return rels

obj = Pingf()
objs = obj.ping(list(map(int,input().split(','))))
print(objs[::-1])