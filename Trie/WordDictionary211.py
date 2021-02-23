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
        def dfs(node, i, word):
            if i == len(word): # base case, word till end(empty)
                return node.word
            if word[i] == '.':
                for c in node.children:
                    if dfs(node.children[c], i + 1, word):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                else:
                    return dfs(node.children[word[i]], i + 1, word)      
        return dfs(self.root, 0, word)

    # soln 1
    def search1(self, word: str) -> bool:
        node = self.root
        self.res = False
        self.dfs1(node, word)
        return self.res
    
    def dfs1(self, node, word):
        if not word: # base case, word till end(empty)
            if node.word:
                self.res = True
            return
        elif word[0] == '.': # sub dot with any children
            for nxt_node in node.children.values():
                self.dfs1(nxt_node, word[1:])
        else: # normal trie
            if word[0] not in node.children: # cannot find nxt char
                return
            node = node.children[word[0]]
            self.dfs1(node, word[1:])
      
    # soln 2      
    def search2(self, word: str) -> bool:
        node = self.root
        return self.dfs2(node, word)
    
    def dfs2(self, node, word):
        if not word: # base case, word till end(empty)
            return node.word

        if word[0] == '.': # sub dot with any children
            for nxt_node in node.children.values():
                if self.dfs2(nxt_node, word[1:]):
                    return True
            return False
        else: # normal trie
            if word[0] not in node.children: # cannot find nxt char
                return False
            node = node.children[word[0]]
            return self.dfs2(node, word[1:])
                
            
        
            
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)