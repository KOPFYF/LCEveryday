class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.word = True
        
    def find(self): # find prefix
        res = []
        def dfs(dirs, node):
            if node.word: # current node is leaf, append prev dirs
                res.append('/' + '/'.join(dirs))
                # print(dirs, res)
                return
            for nxt_node in node.children:
                dfs(dirs + [nxt_node], node.children[nxt_node])
        dfs([], self.root)
        return res
                      
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            f = f.split('/')[1:] # split into list, remove empty
            trie.insert(f)
        return trie.find()