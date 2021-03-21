class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = ""
        cur = ""
        for ch in s:
            if ch == '[':
                stack.append((cur, num))
                num = ""
                cur = ""
            elif ch == ']':
                prev, num = stack.pop()
                cur = prev + int(num) * cur
                num = ""
            elif ch.isdigit():
                num += ch
            else:
                cur += ch
            # print(ch, num, cur)
        return cur