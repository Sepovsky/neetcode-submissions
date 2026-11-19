class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        dig = -1
        ans = []
        for i in range(len(arr) - 1, -1, -1):
            ans.append(dig)
            if arr[i] > dig:
                dig = arr[i]
        return ans[::-1]