class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        for i in range(len(s)):
            l, r = i, i
            ans = ""
            resLen = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    ans = s[l:r+1]
                    resLen = r - l + 1
                    res.append(ans)
                r += 1
                l -= 1
            
            l, r = i, i + 1
            ans = ""
            resLen = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    ans = s[l:r+1]
                    resLen = r - l + 1
                    res.append(ans)
                
                r += 1
                l -= 1
        return len(res)