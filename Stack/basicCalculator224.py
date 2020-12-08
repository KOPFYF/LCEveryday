class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '+':
                res += sign * num
                num = 0
                sign = 1 
            elif c == '-':
                res += sign * num
                num = 0
                sign = -1
            elif c == '(':
                # push the result first, then sign
                stack.append(res)
                stack.append(sign)
                # reset the sign and result for the value in the parenthesis
                sign = 1
                res = 0
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop() # sign before the parenthesis
                res += stack.pop() # the result calculated before the parenthesis
            # print(stack, res, num)
        if num != 0:
            res += sign * num
        return res