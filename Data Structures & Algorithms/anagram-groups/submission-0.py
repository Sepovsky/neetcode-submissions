class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        ang = {}

        for word in strs:
            key = "".join(sorted(word))
            ang.setdefault(key, []).append(word)
        
        return list(ang.values())