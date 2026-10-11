# Claude fixed ver

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']

        cal = []

        for t in tokens:
            if t == '+':
                cal.append(cal.pop() + cal.pop())
            elif t == '-':
                b, a = cal.pop(), cal.pop()
                cal.append(a - b)
            elif t == '*':
                cal.append(cal.pop() * cal.pop())
            elif t == '/':
                b, a = cal.pop(), cal.pop()
                cal.append(int(a / b))
            else:
                cal.append(int(t))

        return cal[0]