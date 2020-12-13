class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = len(s)
        sign = '+'
        i = 0
        
        while i < n:
            if s[i] in '+-*/':
                sign = s[i]
                
            elif s[i].isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1
                if sign in ['-', '+']:
                    sign = 1 if sign == '+' else -1
                    stack.append(sign * num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # stack.append(stack.pop() // num) # "14-3/2"
                    stack.append(int(stack.pop() / num))
                continue
            i += 1
        return sum(stack)