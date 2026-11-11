class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        def hr(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            if n == 2:
                return max(arr[0], arr[1])
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]
        
        return max(hr(nums[1:]), hr(nums[:-1]))