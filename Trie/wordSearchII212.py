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
            
            # After this node is processed, if it has no children, prune it!
            # if not nxt_node:
            #     del node.children[tmp]
            if not nxt_node.children:
                # node.children.pop(tmp)
                del node.children[tmp] # this line would boost it from 7000ms to 28ms

                
 
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




class Trie:
    def __init__(self):
        self.root={}
        return
    
    def insert(self, word:str):
        p=self.root
        for w in word:
            if w not in p:
                p[w]={}
            p=p[w]
        p[""]=None
        return
    

class Solution1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans=[]

        def rec(curr: str, parent: dict, x: int, y: int):
            letter=board[x][y]
            node = parent[letter]
            curr += letter
            if "" in node:
                ans.append(curr)
                # append the curr word to ans
                # del is called to avoid duplicates
                # in ans. without it, for e.g.,
                # oo and oor will end up
                # having 2x"oo" and 1x"oor" in ans
                # since "oo" is common subword during
                # both traversals
                del node[""]
            
            # modify in place to avoid the use of 
            # visited list
            board[x][y]='#'

            neighbors=[(x-1,y),(x,y+1),(x+1,y),(x,y-1)]
            for x0,y0 in neighbors:
                if (0<=x0<len(board) and 0<=y0<len(board[0])
                    and board[x0][y0] != '#'
                    and board[x0][y0] in node):
                    rec(curr, node,x0,y0)
                    
            # restore the modification earlier
            board[x][y]=letter
            
            # After this node is processed,
            # if it has no children - kill it!
            # memory optimization
            if not node:
                del parent[letter]
            
        # insert words into dict
        trie=Trie()
        for word in words:
            trie.insert(word)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root:
                    # Pass parent to recursion
                    # instead of node itself
                    rec("", trie.root,i,j)
        return ans



class Solution_DFS_TLE:
    def findWords(self, board0: List[List[str]], words: List[str]) -> List[str]:
        '''
        m == board.length
        n == board[i].length
        1 <= m, n <= 12
        board[i][j] is a lowercase English letter.
        1 <= words.length <= 3 * 10^4
        1 <= words[i].length <= 10

        O(mn3^lw) = O(12*12*10^3*2*10^4)
        '''
        def findWord(board, word):
            # O(mn3^l) / O(l)
            m, n, w = len(board), len(board[0]), len(word)
        
            def dfs(x, y, pos):
                # return True if we find a valid word
                if pos == w:
                    return True
                tmp, board[x][y] = board[x][y], '#'
                
                res = False
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == word[pos] and dfs(nx, ny, pos + 1):
                            res = True
                board[x][y] = tmp
                return res

            for x in range(m):
                for y in range(n):
                    if board[x][y] == word[0] and dfs(x, y, 1):
                        return True
            return False
        
        res = []
        # O(mn3^lw) TLE
        for word in set(words):
            if findWord(board0, word):
                res.append(word)
        return res




        