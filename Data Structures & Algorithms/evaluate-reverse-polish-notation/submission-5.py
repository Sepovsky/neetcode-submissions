class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def act(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return b - a
            elif op == '*':
                return a * b
            elif op == '/':
                return int(b / a)

        nums = []
        ops = ['+', '-', '*', '/']

        for i in tokens:
            if i in ops:
                q = nums.pop()
                p = nums.pop()
                nums.append(act(q, p, i))
            else:
                nums.append(int(i))

        return nums[-1]