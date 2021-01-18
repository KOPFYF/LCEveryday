# https://leetcode.com/problems/word-squares/discuss/91360/3-Python-Solutions-with-very-detailed-explanations

class Solution_bt: # TLE !!
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # backtracking
        res = []
        if words:
            self.dfs([], len(words[0]), words, res)
        return res
    
    def generate_candidates(self, so_far, words):
        prefix =  "".join([x[len(so_far)] for x in so_far])
        # print(prefix)
        for w in words:
            if w.startswith(prefix):
                yield w

    def dfs(self, so_far, N, words, results):
        # so_far
        if len(so_far) == N:
            results.append([x for x in so_far])
        else:
            for c in self.generate_candidates(so_far, words):
                so_far.append(c)
                self.dfs(so_far, N, words, results)
                so_far.pop()
        return



class Solution_ht(object):
    def helper(self, so_far, N, words, results, table):
        if len(so_far) == N:
            results.append([x for x in so_far])
        else:
            prefix = "".join([x[len(so_far)] for x in so_far])
            for c in table.get_prefix_matches(prefix):
                so_far.append(c)
                self.helper(so_far, N, words, results, table)
                so_far.pop()
        return
    
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        results = []
        if words:
            table = PrefixHashTable(words)
            self.helper([], len(words[0]), words, results, table)
        return results


class PrefixHashTable(object):
    def __init__(self, words):
        self.prefix_table = {}
        for w in words:
            for prefix in (w[0:i] for i in range(len(w))):
                self.prefix_table.setdefault(prefix, set([])).add(w)
        return
    
    def get_prefix_matches(self, prefix):
        candidates = self.prefix_table[prefix] if prefix in self.prefix_table else set([])        
        return candidates
