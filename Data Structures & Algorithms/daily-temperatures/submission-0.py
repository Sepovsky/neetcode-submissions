class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [[0, temperatures[0]]]
        for i in range(1, len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                temp = stack.pop()
                res[temp[0]] = i - temp[0]
            else:
                stack.append([i, temperatures[i]])
        return res


