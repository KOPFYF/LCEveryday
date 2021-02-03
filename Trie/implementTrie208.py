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
        
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False # go down the tree
            node = node.children[ch]
        return True # loop to the end and all good!