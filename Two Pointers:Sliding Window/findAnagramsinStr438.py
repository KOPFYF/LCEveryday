class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # slow af, time O(n), space O(2m) 
#         n, m, i, res = len(s), len(p), 0, []
#         if n < m: return []
#         p_dict, s_dict = Counter(p), Counter(s[: m])

#         while i + m <= n:
#             if p_dict == s_dict:
#             if not len(p_dict - s_dict) and not len(s_dict - p_dict):
#                 res.append(i)
#             s_dict[s[i]] -= 1
#             if i + m < n:
#                 s_dict[s[i + m]] += 1
#             i += 1
#         return res
    
        # 100ms, time O(n), space O(2m) 
        m, cur = [0] * 26, [0] * 26
        res, n = [], len(p)
        for c in p:
            m[ord(c) - ord('a')] += 1
        
        for i, c in enumerate(s):
            cur[ord(c) - ord('a')] += 1
            if i >= n:
                cur[ord(s[i - n]) - ord('a')] -= 1
            if cur == m:
                res.append(i - n + 1)
        return res