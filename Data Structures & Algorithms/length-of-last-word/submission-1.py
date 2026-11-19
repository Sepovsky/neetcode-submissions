class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1 and s != " ":
            return 1
        r = ""
        rev = s[::-1]
        for c in rev:
            if len(r) == 0 and c == " ":
                continue
            if c == " ":
                return len(r)
            r += c