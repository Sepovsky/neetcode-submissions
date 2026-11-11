class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}
        for i in range(n):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        buckets = [[] for i in range(n + 1)]
        for i, cnt in count.items():
            buckets[cnt].append(i)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        