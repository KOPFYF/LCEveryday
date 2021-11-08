class Solution:
    def calculate(self, s: str) -> int:
        # O(n) / O(1)
        s += '+'
        prev = 0 # new var
        num = 0
        total = 0 # new var
        prev_sign = '+'
        
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-*/':
                if prev_sign == '+':
                    total += num
                    prev = num
                elif prev_sign == '-':
                    total -= num
                    prev = -num
                elif prev_sign == '*':
                    # reverse one operation, 2 + 3 * 2
                    #                          prev  num
                    total -= prev
                    total += prev * num
                    prev = prev * num
                elif prev_sign == '/':
                    # reverse one operation, 2 + 3 / 2
                    #                          prev  num
                    total -= prev
                    total += int(prev / num)
                    prev = int(prev / num)
                
                prev_sign = ch
                num = 0
        return total

class Solution:
    def calculate(self, s: str) -> int:
        # O(n) / O(n)
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