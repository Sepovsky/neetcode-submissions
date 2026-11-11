class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        store = -1
        while i < j:
            store = max(store, (min(heights[i], heights[j]) * (j - i)))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return store
            