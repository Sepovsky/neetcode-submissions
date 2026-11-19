class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ans = 0
        for char in t:
            if ans == len(s):
                break
            
            if s[ans] == char:
                ans += 1
        return ans == len(s)