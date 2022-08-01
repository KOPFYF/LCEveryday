class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # slow af, time O(n), space O(2m) 
        n, m, i, res = len(s), len(p), 0, []
        if n < m: return []
        p_dict, s_dict = Counter(p), Counter(s[: m])

        while i + m <= n:
            if p_dict == s_dict:
            if not len(p_dict - s_dict) and not len(s_dict - p_dict):
                res.append(i)
            s_dict[s[i]] -= 1
            if i + m < n:
                s_dict[s[i + m]] += 1
            i += 1
        return res
    
        # time O(s), space O(26)
        dic, cur = [0] * 26, [0] * 26
        res, n = [], len(p)
        for ch in p:
            dic[ord(ch) - ord('a')] += 1
            
        for i, ch in enumerate(s):
            cur[ord(ch) - ord('a')] += 1
            if i >= n:
                cur[ord(s[i - n]) - ord('a')] -= 1
            if cur == dic: # O(1)
                res.append(i - n + 1)
        
        return res