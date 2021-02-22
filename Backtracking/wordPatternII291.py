'''
We divide the sub-problem as self.helper(pattern, str, i, j) to answer if str[j:] follows the same pattern[i:].
You need to be careful in the backtracking part where you delete ptable and stable. 
There are two conditions when you proceed with the recursion: 
when both ptable and stable have the right mapping and when both are empty. 
In the latter instance, you add the mapping, therefore, you delete only when under those circumstances. 
Otherwise you can end up with an error.
'''

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.dfs2(pattern, s, 0, 0, {}, {})
    
    def dfs(self, pattern, s, i, j, ptable, stable):
        if i == len(pattern) and j == len(s):
            return True # 2 pointers both to the end
        if i == len(pattern) or j == len(s):
            return False
        
        p, added = pattern[i], False
        for k in range(j, len(s)):
            word = s[j:k+1]
            # Test is using the word violates the rules learned thus far!
            if (p in ptable and ptable[p] != word) or (word in stable and stable[word] != p):
                continue # skip current word because no mapping found!
            # added variable ensures we only remove from dictionary when we had previously added.
            if p not in ptable and word not in stable: # build the mapping
                ptable[p], stable[word], added = word, p, True
            remainder = self.dfs(pattern, s, i + 1, k + 1, ptable, stable)
            if added:
                del ptable[p]
                del stable[word]
            if remainder:
                return True
        return False
    
    def dfs2(self, pattern, str, i, j, ptable, stable):
        if i == len(pattern) and j == len(str):
            return True
        if i == len(pattern) or j == len(str):
            return False
        p = pattern[i]
        for k in range(j, len(str)):
            word = str[j:k+1]
            if (p in ptable and ptable[p] != word) or (word in stable and stable[word] != p):
                continue # skip inconsistent mapping!
            n_ptable, n_stable = {k1:v1 for k1,v1 in ptable.items()}, {k1:v1 for k1,v1 in stable.items()}
            n_ptable[p], n_stable[word] = word, p
            remainder = self.dfs2(pattern, str, i+1, k+1, n_ptable, n_stable)
            if remainder:
                return True
        return False