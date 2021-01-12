class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # rolling hash, O(n)
        base, aL, idx, mod, n = 26, 1, 0, 10 ** 9 + 7, len(s)
        hash1, hash2 = 0, 0 # left2right vs right2left
        nums = [ord(s[i]) - ord('a') for i in range(n)]
        
        for i in range(n):
            hash1 = (hash1 * base + nums[i]) % mod
            hash2 = (hash2 + aL * nums[i]) % mod
            aL = aL * base % mod
            if hash1 == hash2:
                idx = i
        return s[idx + 1:][::-1] + s



class Solution_tricky:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # greedy search, O(n^2)
        n = len(s)
        t = s[::-1]
        for i in range(n,-1,-1):
            if s[:i] == t[n-i:]:
                break
        return t[:n-i] + s