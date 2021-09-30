class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        self.n = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node = self.root
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if node.n < 3:
                node.n += 1
                node.words.append(word)
    
    def search_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return ''
            node = node.children[ch]
        return node.words
    
    def search_prefix2(self, c):
        if self.node and c in self.node.children: 
            self.node = self.node.children[c] 
            return self.node.words
        else: 
            self.node = None    
            return []
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # lexicographically minimums products so need to sort
        products.sort()
        trie = Trie()
        for word in products:
            trie.insert(word)
        
        res, pre = [], ''
        for ch in searchWord:
            pre += ch
            res.append(trie.search_prefix(pre))
        return res


class Solution2:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for word in products: 
            trie.insert(word)

        return [trie.search_prefix2(c) for c in searchWord]