class TrieNode:
    '''
    prefixCnt, how many words start with prefix whose last node is current node.
    wordCnt, how many words end with current node.
    '''
    def __init__(self):
        self.isWord = False
        self.children = {}
        self.pcnt = 0 # prefix count
        self.wcnt = 0 # word count

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root 
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.pcnt += 1
        node.isWord = True
        node.wcnt += 1
        
    def countWordsEqualTo(self, word: str) -> int:
        node = self.root 
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.wcnt
        
    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root 
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.pcnt
        
    def erase(self, word: str) -> None:
        node = self.root 
        for ch in word:
            node = node.children[ch]
            node.pcnt -= 1
        node.wcnt -= 1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)