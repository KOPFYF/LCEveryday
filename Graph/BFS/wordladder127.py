class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        wordList = set(wordList)    
        if endWord not in wordList:
            return 0
        charList = set(w for word in wordList for w in word)
        bfs = deque([(beginWord, 0)])
        
        while bfs:
            curWord, depth = bfs.popleft()
            if curWord == endWord: 
                return depth + 1 # actually return next level
            for i in range(len(curWord)):
                for c in charList:
                    nxtWord = curWord[:i] + c + curWord[i + 1:]
                    if nxtWord in wordList:
                        bfs.append((nxtWord, depth + 1))
                        wordList.remove(nxtWord) # avoid cycle
        return 0