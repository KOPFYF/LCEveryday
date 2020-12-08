class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # keep a increasing stack
        if k == len(num): return "0"
        
        stack = []
        for i, ch in enumerate(num):
            while stack and stack[-1] > ch and k > 0:
                stack.pop()
                k -= 1
            stack.append(ch)
        if k > 0: 
            # cases like "112" k = 1, the mono-inc stack would be [1,1,2]
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"