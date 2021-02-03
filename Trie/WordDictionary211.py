class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch] # move on to the nxt level
        node.word = True # loop to the end, store the word as true
        

    def search(self, word: str) -> bool:
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word: # base case, word till end(empty)
            if node.word:
                self.res = True
            return
        elif word[0] == '.': # sub dot with any children
            for nxt_node in node.children.values():
                self.dfs(nxt_node, word[1:])
        else: # normal trie
            if word[0] not in node.children: # cannot find nxt char
                return
            node = node.children[word[0]]
            self.dfs(node, word[1:])