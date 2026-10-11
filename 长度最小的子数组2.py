class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        i= 0
        max_l = -1
        res = {}
        for j in range(len(fruits)):
            res[fruits[j]] = res.get(fruits[j],0) + 1
            while len(res) > 2:
                res[fruits[i]] -= 1
                if res[fruits[i]] == 0:
                    del res[fruits[i]]
                i += 1
            max_l = max(max_l,j - i + 1)
        return max_l