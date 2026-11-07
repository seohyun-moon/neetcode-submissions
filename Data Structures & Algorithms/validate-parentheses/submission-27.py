class Solution:
    def isValid(self, s: str) -> bool:
        couple = {'(': ')', '{': '}', '[':']'}

        stack = []

        for c in s:
            if c in couple:
                stack.append(c)
            else:
                if stack and couple[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return not stack