class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = s.replace(" ", "")
        cs = "".join(char for char in cs if char.isalnum())
        cs = cs.lower()
        
        return cs == cs[::-1]