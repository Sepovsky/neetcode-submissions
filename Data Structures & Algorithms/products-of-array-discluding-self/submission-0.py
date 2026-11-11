class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n 
        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        sofix = [0] * n
        sofix[n-1] = 1
        for i in range(len(nums)-2, -1, -1):
            sofix[i] = sofix[i+1] * nums[i+1]
        
        res = [0] * n
        for i in range(len(sofix)):
            res[i] = sofix[i] * prefix[i]
        
        return res