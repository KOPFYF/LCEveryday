class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        cur = ""
        for ch in s:
            if ch.isdigit():
                num = 10 * num + int(ch)
            elif ch == '[':
                stack.append((cur, num))
                cur = ''
                num = 0
            elif ch == ']':
                prev, prev_num = stack.pop()
                cur = prev + prev_num * cur
            else:
                cur += ch
            # print(ch, stack, cur, num)
        return cur