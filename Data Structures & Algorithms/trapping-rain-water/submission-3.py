class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        suf = []
        mx = height[0]
        for i in range(len(height)):
            if height[i] > mx:
                mx = height[i]
            pre.append(mx)
        
        hs = height[::-1]
        mx = height[-1]
        for i in range(len(height)):
            if hs[i] > mx:
                mx = hs[i]
            suf.append(mx)
        suf.reverse()

        ans = 0
        for i in range(len(height)):
            ans +=  max(min(pre[i], suf[i]) - height[i], 0)
        return ans