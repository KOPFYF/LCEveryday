# Remove Sub-Folders from the Filesystem


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, path):
        node = self.root
        for f in path.split('/')[1:]:
            if f not in node.children:
                node.children[f] = TrieNode()
            node = node.children[f]
        node.isEnd = True
    
    def search(self):
        res = []
        def dfs(node, path):
            if node.isEnd:
                res.append('/' + '/'.join(path)) # if there are multiple ends in current path, only return the shallow one
                return
            for f in node.children:
                nxt_node = node.children[f]
                dfs(nxt_node, path + [f])
        dfs(self.root, [])
        return res
                
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for path in folder:
            trie.insert(path)
            
        return trie.search()