class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {"]":"[", "}":"{", ")":"("}
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if not stack or d[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return stack == []