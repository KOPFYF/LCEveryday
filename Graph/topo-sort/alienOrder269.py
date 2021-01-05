class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indegrees = {c : 0 for word in words for c in word}
        for word1, word2 in zip(words, words[1:]):
            # cmp adj 2 words
            if len(word2) < len(word1) and word1[:len(word2)] == word2:
                return "" # abcd, abc, in such case no solution
            for c1, c2 in zip(word1, word2):
                # find the first diff pair
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].append(c2)
                        indegrees[c2] += 1
                    break # one diff is enough
        
        # bfs
        res = []
        bfs = deque([c for c, v in indegrees.items() if v == 0])
        while bfs:
            cur = bfs.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    bfs.append(nxt)
        
        # end condition:
        #  - sum(indegrees.values()) == 0
        #  - len(res) == len(indegrees) == len(nodes)
        if sum(indegrees.values()) > 0:
            return ""
        return "".join(res)


word1 = 'abcd'
word2 = 'abc'
for c1, c2 in zip(word1, word2):
    print(c1, c2) # end with shorter one