class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # 2 Pointers, time O(n) space O(n)
        d = {c:i for i, c in enumerate(S)} # hash table record last index
        l, r, res = 0, 0, []
        
        for idx, s in enumerate(S):
            r = max(r, d[s]) # grow right pointer to the last index
            if idx == r: # meet chunk, cut and reset
                res.append(r - l + 1)
                l = idx + 1
                
        return res