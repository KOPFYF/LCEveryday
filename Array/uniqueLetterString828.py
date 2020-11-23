class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type s: str
        :rtype: int
        """
        # index[26][2] record last two occurrence index for every upper characters.
        # Initialise all values in index to -1.
        # Loop on string S, for every character c, update its last two occurrence index to index[c].
        # Count when loop. For example, if "A" appears twice at index 3, 6, 9 seperately, we need to count:
        # For the first "A": (6-3) * (3-(-1))
        # For the second "A": (9-6) * (6-3)
        # For the third "A": (N-9) * (9-6)
        index = {c: [-1, -1] for c in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(S):
            k, j = index[c]
            res += (i - j) * (j - k)
            index[c] = [j, i]
        for c in index:
            k, j = index[c]
            res += (len(S) - j) * (j - k)
        return res % (10**9 + 7)