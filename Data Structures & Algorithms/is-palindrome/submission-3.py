class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = s.replace(" ", "")
        cs = "".join(char for char in cs if char.isalnum())
        cs = cs.lower()
        n = len(cs)
        i, j = 0, n-1
        if n is 0:
            return True
        while i!=j and i < (n//2) + 1:
            if cs[i] == cs[j]:
                i += 1
                j -= 1
            else:
                return False
        return True