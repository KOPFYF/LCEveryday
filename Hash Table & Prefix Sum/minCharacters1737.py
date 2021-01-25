'''
The third condition is trivial to check.

For the first condition, we loop thru each possible character, so at first we consider making all elements in first string less than b (so all should be a). Then all elements in second string less than b should be converted. This requires len(a) - ha[1] + hb[1] changes, and so on. (Characters are mapped to their occurrence locations in the code, so a is 1, b is 2, etc.)

Remember to skip last entry, so loop runs from 1,...,25 and not 1,...26. If you got an error during testing in the contest, this is probably the reason (and hidden test cases do not help ;)).

Second condition is symmetric.
'''


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # O(m + n)/O(26)
        m, n = len(a), len(b)
        c1 = Counter(ord(c) - 97 for c in a)
        c2 = Counter(ord(c) - 97 for c in b)
        res = m + n - max((c1 + c2).values()) # condition 3
        for i in range(25):
            c1[i + 1] += c1[i]
            c2[i + 1] += c2[i]
            res = min(res, m - c1[i] + c2[i]) # condition 1
            res = min(res, n - c2[i] + c1[i]) # condition 2
        return res