class TrieNode:
    def __init__(self, char = '', val = 0):
        self.children = {}
        self.val = val
        self.char = char

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        # update dict
        if key in self.d:
            prev = self.d[key]
            self.d[key] = val # overridden to the new one
            # they already exist in our trie tree
            val -= prev # for trie tree update, use delta
        else:
            self.d[key] = val
            
        # update trie tree
        i, l = 0, len(key)
        cur = self.root
        while i < l:
            char = key[i]
            if char not in cur.children:
                cur.children[char] = TrieNode(char, val)
            else:
                cur.children[char].val += val
            cur = cur.children[char]
            i += 1
            

    def sum(self, prefix: str) -> int:
        i, l = 0, len(prefix)
        cur = self.root
        while i < l:
            char = prefix[i]
            if char not in cur.children:
                return 0
            cur = cur.children[char]
            i += 1
        return cur.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)