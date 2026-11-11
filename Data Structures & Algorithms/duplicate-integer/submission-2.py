class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(list(set(nums)))