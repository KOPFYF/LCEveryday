class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, trie, m, n = [], Trie(), len(board), len(board[0])
        for word in words:
            trie.insert(word)
        for i in range(m):
            for j in range(n):
                self.dfs(board, trie.root, i, j, "", res, m, n)
        return res
    
    def dfs(self, board, node, x, y, path, res, m, n):
        if node.word:
            res.append(path)
            node.word = False # find a word and marked as visited
        if 0 <= x < m and 0 <= y < n:
            tmp = board[x][y]
            if tmp not in node.children:
                return
            node = node.children[tmp] # go down
            board[x][y] = '#'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                self.dfs(board, node, nx, ny, path + tmp, res, m, n)
            board[x][y] = tmp
 

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie: #  prefix tree(字典🌲)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch] # move on to the nxt level
        node.word = True # loop to the end, store the word as true
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False # go down the tree
            node = node.children[ch]
        return node.word