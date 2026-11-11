class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        res = []

        for i in range(len(sort_nums)):
            target = -(sort_nums[i])
            l, r = i + 1, len(sort_nums) - 1
            while l < r:
                tmp = sort_nums[l] + sort_nums[r]
                if tmp < target:
                    l += 1
                elif tmp > target:
                    r -= 1
                elif tmp == target:
                    res.append([sort_nums[i], sort_nums[l], sort_nums[r]])
                    l += 1
                    r -= 1
        res = [list(x) for x in set(map(tuple, res))]
        return res