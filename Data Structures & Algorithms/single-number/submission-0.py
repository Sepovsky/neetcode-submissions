class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map_num = defaultdict(int)
        for i in nums:
            map_num[i] += 1
        
        for i in nums:
            if map_num[i] == 1:
                return i
