class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # BFS, O(nw)
        wordSet = set(wordList)    
        if endWord not in wordSet: return []
        charSet = set(ch for word in wordSet for ch in word)
        bfs = defaultdict(list) 
        bfs[beginWord] = [[beginWord]] # key is current word, value is 2d paths
        while bfs:
            nxt_bfs = defaultdict(list)
            for word in bfs:
                if word == endWord: return bfs[word]
                for i in range(len(word)):
                    for ch in charSet:
                        nxt_word = word[:i] + ch + word[i+1:]
                        if nxt_word in wordSet:
                            nxt_bfs[nxt_word] += [path + [nxt_word] for path in bfs[word]] 
            # to find all paths, node can be revisited in the same level, image those paths are parallelized
            # need to find all paths, cannot use a visited set globally !!
            wordSet -= set(nxt_bfs.keys())
            bfs = nxt_bfs
        return []


## Solution 1
class Solution1:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # BFS, O(nw)
        wordSet = set(wordList)    
        if endWord not in wordSet: return []
        charSet = set(ch for word in wordSet for ch in word)
        res, bfs, visited = [], deque([(beginWord, [beginWord])]), set([beginWord])
        while bfs:
            tmp_visited = set() # use a tmp visited set and update level by level
            size = len(bfs)
            for _ in range(size):
                word, path = bfs.popleft()
                if word == endWord: res += [path]
                for i in range(len(word)):
                    for ch in charSet:
                        nxt_word = word[:i] + ch + word[i+1:]
                        if nxt_word in wordSet and nxt_word not in visited:
                            tmp_visited.add(nxt_word)
                            bfs.append((nxt_word, path + [nxt_word]))
            visited |= tmp_visited
        return res