class Solution:
    def isValid(self, s: str) -> bool:
        def checker(a, b):
            if a == '[' and b == ']':
                return True
            elif a == '(' and b == ')':
                return True
            elif a == '{' and b == '}':
                return True
            else:
                return False
            
        opener = ['(', '[', '{']
        closer = ['}', ']', ')']

        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue
            
            char = stack.pop()
            if not checker(char, i):
                stack.append(char)
                stack.append(i)
        
        if len(stack):
            return False
        else:
            return True

