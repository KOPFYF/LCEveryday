class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2 Pointers, time O(n), space O(n)
        i = res = 0
        d = {} # record the latest index of char
        
        for j, c in enumerate(s):
            if c in d and i <= d[c]: 
                # if seen repeat char, relocate left = right + 1
                # i <= d[c] to avoid case like "tmmzxta", in which 2nd 't' should consider as not seen
                # i = 2(dup 'm'), d['t'] = 0, so dont go into this if condition
                # d[c] >= i means 'c' is in the being considered substring s[i, j]
                i = d[c] + 1
            
            res = max(res, j - i + 1)
            d[c] = j # update the latest index
            
        return res


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2 Pointers, time O(n), space O(n)
        i = res = 0
        d = {} # record the latest index of char
        
        for j, c in enumerate(s):
            if c in d : # and i <= d[c]: 
                # if seen repeat char, relocate left = right + 1
                # i <= d[c] to avoid case like "tmmzxta", in which 2nd 't' should consider as not seen
                # i = 2(dup 'm'), d['t'] = 0, so dont go into this if condition
                # d[c] >= i means 'c' is in the being considered substring s[i, j]
                i = max(d[c] + 1, i) # i cannot go backward
                print(c, i, j, res)
            print(i, j, s[i:j+1])
            res = max(res, j - i + 1)
            d[c] = j # update the latest index
            
        return res