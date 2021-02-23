class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
        self.words = []

class Trie: #  prefix tree(字典🌲)
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self.root
        node.words.append(word)
        for ch in word:
            node = node.children[ch] # move on to the nxt level
            node.words.append(word)
        node.isWord = True # loop to the end, store the word as true
        # node.string = word
        
    def allWords(self, prefix):
        # return all possible words with current prefix
        node = self.root
        for ch in prefix:
            if not node.children.get(ch, None):
                return [] # go down the tree
            node = node.children[ch]
        return node.words
        

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res, k, trie = [], len(words[0]), Trie(words)

        def dfs(row, matrix):
            # row means last row index + 1
            if row == k:
                res.append(matrix)
                return
            prefix = ''.join(r[row] for r in matrix)
            for word in trie.allWords(prefix):
                dfs(row + 1, matrix + [word]) # pass by val
                
        def dfs2(row, matrix):
            # row means last row index + 1
            if row == k:
                res.append(matrix[:]) # matrix is passed by ref, need a shallow-copy
                return
            prefix = ''.join(r[row] for r in matrix)
            for word in trie.allWords(prefix):
                matrix.append(word)
                dfs(row + 1, matrix) # pass by ref
                matrix.pop()
        
        dfs(0, [])
        return res

# https://stackoverflow.com/questions/4081561/what-is-the-difference-between-list-and-list-in-python
# When reading, list is a reference to the original list, and list[:] shallow-copies the list.
# When assigning, list (re)binds the name and list[:] slice-assigns, replacing what was previously in the list.


        
        
        
        
    