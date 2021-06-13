class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        d = collections.defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website), key=lambda x:x[1]):
            d[u].append(w)
        
        count = defaultdict(int)
        for webs in d.values():
            combs = set(itertools.combinations(webs, 3))
            for comb in combs:
                count[comb] += 1
        
        # sort the Counter by freq and return the max freq item
        return sorted(count, key=lambda x:(-count[x], x))[0]