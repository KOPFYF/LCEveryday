class Solution_trie_shorter:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        numWordsBegin = defaultdict(int)
        
        def insert(word):
            nonlocal trie
            tmp = trie
            for c in word:
                if c not in tmp:
                    tmp[c] = defaultdict()
                tmp = tmp[c] 
            tmp['#'] = word
        
        for word in words:
            numWordsBegin[word[0]] += 1
            insert(word)
        
        row = len(board)
        col = len(board[0])
        res = set()
        
        def dfs(i,j,tmp):
            if '#' in tmp:
                res.add(tmp['#'])
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            
            w = board[i][j]
            if w not in tmp:
                return
            
            board[i][j] = '0'
            dfs(i-1,j,tmp[w])
            dfs(i+1,j,tmp[w])
            dfs(i,j-1,tmp[w]) 
            dfs(i,j+1,tmp[w])
            board[i][j] = w            
            
        
        for i in range(row):
            for j in range(col):
                dfs(i,j,trie)
                    
        return list(res)


class Solution_trie:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, trie = [], Trie() 
        m, n, node = len(board), len(board[0]), trie.root
        for word in words:
            trie.insert(word)
        for i in range(m):
            for j in range(n):
                self.dfs(board, node, i, j, "", res, m, n)
        return res
    
    def dfs(self, board, node, x, y, path, res, m, n):
        if node.word:
            res.append(path)
            node.word = False # find a word and marked as visited
        if 0 <= x < m and 0 <= y < n:
            tmp = board[x][y]
            if tmp not in node.children:
                return
            nxt_node = node.children[tmp] # go down
            board[x][y] = '#'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                self.dfs(board, nxt_node, nx, ny, path + tmp, res, m, n)
            board[x][y] = tmp
            
            # After this node is processed, if it has no children, kill it!
            # if not nxt_node:
            #     del node.children[tmp]
            if not nxt_node.children:
                del node.children[tmp]
                # node.children.pop(tmp)              
 
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie: #  prefix tree(字典\U0001f332)
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



class Solution_pure_dfs_tle:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # TLE on the last case in July 2021
        words = set(words)
        m, n = len(board), len(board[0])
        res = []
        def dfs(i, j, l, word):
            if word[l] != board[i][j]: 
                return False
            if l + 1 == len(word): 
                return True
            
            tmp = board[i][j]
            board[i][j] = '#'
            res = False
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    res = res or dfs(x, y, l + 1, word)
            board[i][j] = tmp
            return res
        
        res = set()
        for word in words:
            for i in range(m):
                for j in range(n):
                    if dfs(i, j, 0, word):
                        res.add(word)
        # print(res)
        return list(res)