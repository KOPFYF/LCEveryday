'''
Use a stack and move from right to left in the string. Push the digits on the stack, ignore ":", and when you you encounter "?", test whether the character preceeding it is T or F. Depending on that, pop values from the stack and evaluate the expression and then push it back.
The key insight is that we need to find the first "?" while going right to left, evaluate it, and then push it back into the stack.
'''

class Solution:
    def parseTernary(self, expression: str) -> str:
        i = len(expression)-1
        st = []
        while i >= 0:
            ch = expression[i]
            if ch.isdigit():
                st.append(ch)
                i -= 1
            elif ch in ("T", "F"):
                st.append(ch)
                i -= 1
            elif ch == ":":
                i -= 1
            elif ch == "?":
                i -= 1
                true = st.pop()
                false = st.pop()
                if expression[i] == "T":
                    st.append(true)
                else:
                    st.append(false)
                i -= 1
            # print(st)
        return st[-1]