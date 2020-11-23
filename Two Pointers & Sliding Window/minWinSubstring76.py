class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 2 pointers, time O(n), space O(n)
        d = Counter(t) # target hashmap we need to fullfill
        i, j, found = 0, len(s) - 1, 0
        min_win = ""
        for j in range(len(s)):
            if d[s[j]] > 0: # every time we find the dict value is +, it means we found another one
                found += 1
            d[s[j]] -= 1 # non-target char will be negative
            while found == len(t):
                # print(i, j, d)
                if not min_win or j - i + 1 < len(min_win):
                    # find a more optimal solution
                    min_win = s[i:j+1]
                d[s[i]] += 1 # move left pointer
                if d[s[i]] > 0:
                    found -= 1 # recover cnt for left pointer
                i += 1
            
        return min_win