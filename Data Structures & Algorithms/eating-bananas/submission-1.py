class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        M = max(piles)
        if h == n:
            return M
            
        l, r = 1, M
        def hChecker(piles, rate):
            res = 0
            for i in piles:
                res += i // rate
                if i % rate > 0:
                    res += 1
            return res

        while l <= r:
            m = l + (r - l) // 2
            if hChecker(piles, m) > h:
                l = m + 1
            else:
                r = m - 1
        return l