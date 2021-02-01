class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        wordSet = set(wordList)    
        if endWord not in wordSet: return 0
        charSet = set(ch for word in wordSet for ch in word)
        seen, bfs = set(beginWord), deque([(beginWord, 0)])
        while bfs:
            word, step = bfs.popleft() 
            if word == endWord: return step + 1
            for i in range(len(word)):
                for ch in charSet:
                    nxt_word = word[:i] + ch + word[i+1:]
                    if nxt_word not in seen and nxt_word in wordSet:
                        print(nxt_word)
                        seen.add(nxt_word)
                        bfs.append((nxt_word, step + 1))
        return 0