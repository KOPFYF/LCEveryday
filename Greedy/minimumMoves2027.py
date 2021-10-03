class Solution:
    def minimumMoves(self, s: str) -> int:
        # s = 'O' + s + 'O'
        n = len(s)
        res = 0
        i = 0
        while i < n:
            # print(i, s[i])
            if s[i] == 'X':
                # print(i)
                res += 1
                i += 3
            else:
                i += 1
        return res
                