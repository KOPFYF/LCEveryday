class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = True
        
    def longest_word(self):
        def dfs(node, path):
            # up untill current node, what is the longest string
            # print(path)
            res = path
            for ch, nxt_node in node.children.items():
                if nxt_node.word:
                    tmp = dfs(nxt_node, path + ch)
                    if len(tmp) > len(res):
                        res = tmp
                    elif len(tmp) == len(res) and tmp < res:
                        res = tmp
            return res
        return dfs(self.root, '')
                        
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.longest_word()