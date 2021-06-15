class Solution:
    def longestWord(self, words: List[str]) -> str:
        self.res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dfs(node, path):
            if not node.children: # to the leaf, stop
                self.res.append(''.join(path))
                return 
            for ch in node.children:
                if ''.join(path) + ch in words: # current path in words
                    path.append(ch)
                    dfs(node.children[ch], path)
                    path.pop()
                else: # not in words, stop here
                    self.res.append(''.join(path))
        
        dfs(trie.root, []) # find all possible words
        # print(self.res)
        if self.res:
            return sorted(self.res, key=lambda x:(-len(x), x))[0]
        return ""
        

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie: #  prefix tree(字典🌲)
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch] # move on to the nxt level
        node.word = True # loop to the end, store the word as true
        
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False # go down the tree
            node = node.children[ch]
        return node.word