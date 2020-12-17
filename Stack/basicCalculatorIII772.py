class Solution:
    def calculate(self, s: str) -> int:
        # stack + recursion
        s = s + "$"
        def helper(stack, i):
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                if c.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                elif c == '(': # start a new stack
                    num, i = helper([], i + 1)
                else:
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack.append(stack.pop() * num)
                    if sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stack), i
                    sign = c 
            return sum(stack)
        return helper([], 0)


class Solution:
    def calculate(self, s: str) -> int:
        # 2 stacks
        stack, sign, num = [], '+', 0
        for i, c in enumerate(s + '+'):
            if c.isdigit():
                num = num * 10 + int(c) 
            elif c == '(':
                stack.append(sign)
                stack.append('(')
                sign = '+'
            elif c in '+-*/)':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                if c == ')':
                    num, item = 0, stack.pop()
                    while item != '(':
                        num += item
                        item = stack.pop()
                    sign = stack.pop()
                else:
                    sign, num = c, 0
        return sum(stack)







