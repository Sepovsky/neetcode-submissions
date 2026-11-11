class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for r, h in enumerate(heights + [0]):
            start = r
            while stack and h < stack[-1][1]:
                l, last = stack.pop()
                ans = max(ans, last * (r - l))
                start = l
            stack.append((start, h))
        return ans