class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {val:i for i, val in enumerate(nums)}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ht and ht[diff] != i:
                return [i, ht[diff]]