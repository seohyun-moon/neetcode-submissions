# Claude fixed ver

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']

        cal = []

        for t in tokens:
            if t in operators:
                b = cal.pop()
                a = cal.pop()
                if t == '+':
                    cal.append(a + b)
                elif t == '-':
                    cal.append(a - b)
                elif t == '*':
                    cal.append(a * b)
                else:
                    cal.append(int(a / b))
            else:
                cal.append(int(t))

        return cal[0]