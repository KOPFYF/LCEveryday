class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        
        wordList = set(wordList)
        res = []
        charset = {w for word in wordList for w in word}
        bfs = {} # a dict, key is the current word, values is a 2d list
        bfs[beginWord] = [[beginWord]] # store cur word and all paths to it
        while bfs:
            nxt_bfs = collections.defaultdict(list)
            for word in bfs:
                if word == endWord:
                    return bfs[word]
                for i in range(len(word)):
                    for c in charset:
                        next_word = word[:i] + c + word[i+1:] 
                        if next_word in wordList:
                            # add new word to all sequences and form new layer element
                            nxt_bfs[next_word] += [j + [next_word] for j in bfs[word]]
            wordList -= set(nxt_bfs.keys()) # dedup to prevent inf loop
            bfs = nxt_bfs

        return []