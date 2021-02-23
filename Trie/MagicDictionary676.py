class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        self.change_once_flag = False
        return self.dfs(self.trie.root, 0, searchWord)
    
    def dfs(self, node, pos, word):
        if pos == len(word): return node.word and self.change_once_flag
        if self.change_once_flag:
            if word[pos] in node.children:
                return self.dfs(node.children[word[pos]], pos+1, word)
            else:
                return False
        else:
            for c in node.children: # try to change in this level
                self.change_once_flag = (c != word[pos])
                if self.dfs(node.children[c], pos+1, word):
                    return True
            return False
                
            
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
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)