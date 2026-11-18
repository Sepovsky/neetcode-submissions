class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 11:
            return []
        seen = set()
        repeat = set()

        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub in seen:
                repeat.add(sub)
            else:
                seen.add(sub)
        return list(repeat)
