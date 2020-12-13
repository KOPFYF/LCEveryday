class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        # Iterative with Stack
        stack = [] # stores all chars except ',' and ')'
        for c in expression:
            if c == ')':
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop() # pop '('
                operator = stack.pop()
                stack.append(all(seen) if operator == '&' \
                             else any(seen) if operator == '|' \
                             else not seen.pop())
            elif c != ',':
                # append t or f or left curly bracket
                stack.append(True if c == 't' else False if c == 'f' else c)
            # print(stack)
        return stack.pop()