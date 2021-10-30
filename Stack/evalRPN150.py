class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+': lambda a, b: a + b, \
               '-': lambda a, b: a - b, \
               '*': lambda a, b: a * b, \
               '/': lambda a, b: int(a / b)
              }
        
        stack = []
        for token in tokens:
            if token in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                num = ops[token](num1, num2)
                stack.append(num)
            else:
                stack.append(int(token))
        # print(stack)
        return stack.pop() # stack[-1]