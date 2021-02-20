class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # middle digits + (-1, 0, or 1) flipped into a palindrome.
        l = len(n)
        # with different digits width, it must be either 10...01 or 9...9
        candidates = set((str(10 ** l + 1), str(10 ** (l - 1) - 1)))
        # the closest must be in middle digit +1, 0, -1, then flip left to right
        prefix = int(n[:(l + 1)//2])
        for i in map(str, (prefix - 1, prefix, prefix + 1)):
            # print(i, i[:-1], [i, i[:-1]][l & 1])
            # [i, i[:-1]][l & 1] becomes [i, i[:-1]][0] if l is even and [i, i[:-1]][1] if l is odd
            candidates.add(i + [i, i[:-1]][l & 1][::-1])
        candidates.discard(n) # not including itself
        # If there is a tie, return the smaller one as answer.
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))