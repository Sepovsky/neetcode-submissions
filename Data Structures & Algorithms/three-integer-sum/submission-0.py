class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            target = -(sorted_nums[i])
            j, k = i + 1, len(sorted_nums) - 1
            while j < k:
                tmp = sorted_nums[j] + sorted_nums[k]
                if tmp < target:
                    j += 1
                elif tmp > target:
                    k -= 1
                elif tmp == target:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j += 1
                    k -= 1
        res = [list(x) for x in set(map(tuple, res))]
        return res

        