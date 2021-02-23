class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class AutocompleteSystem1:
    '''
    storing all the words at each node, it increases space but makes the solution around 5 times faster.
    '''

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = TrieNode()
        self.cache_count = defaultdict(int)
        self.keyword = ""
        for i, sen in enumerate(sentences):
            self._insert(sen, self.trie)
            self.cache_count[sen] = times[i]

    def _insert(self, word, trie):
        for ch in word:
            if ch not in trie.children:
                trie.children[ch] = TrieNode()
            trie = trie.children[ch]
            trie.words.append(word)
        return True
    
    def _search(self, word):
        trie = self.trie
        for ch in word:
            if ch not in trie.children:
                return []
            trie = trie.children[ch]
        return trie.words 
        
    def input(self, c: str) -> List[str]:
        if c != '#':
            self.keyword += c
            sens = self._search(self.keyword)
            res = []
            for sen in sens:
                res.append((self.cache_count[sen], sen))
            res = list(set(res))
            return [sen for cnt, sen in sorted(res, key=lambda x:(-x[0], x[1]))[:3]]
        else:
            self.cache_count[self.keyword] += 1
            self._insert(self.keyword, self.trie)            
            self.keyword = ""
        return []




# soln 2
class TrieNode():
    def __init__(self):
        self.isEnd = False
        self.children = {}
        self.hot = 0
    
class AutocompleteSystem2(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.searchTerm = ""
        # 1. add historical data
        for i, sentence in enumerate(sentences):
            self.add(sentence, times[i])
            
    def add(self,sentence, hot):
        node = self.root
        #2. for each character in sentence
        for c in sentence: 
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        #3. when last character is added,
        #   make node.isEnd = True indicate that the current node is end of the sentence
        node.isEnd = True
        #4. do -= because by negating, we can sort as ascending order later
        node.hot-= hot
        
    def search(self):
        node = self.root
        res = []
        path = ""

        for c in self.searchTerm:
            if c not in node.children:
                return res
            # 6. add each character to path variable, path will added to res when we found node.isEnd ==True
            path +=c
            node = node.children[c]
        # 7. at this point, node is at the given searchTerm.
        # for ex. if search term is "i_a", we are at "a" node.
        # from this point, we need to search all the possible sentence by using DFS
        self.dfs(node, path,res)
        # 11. variable res has result of all the relevant sentences
        # we just need to do sort and return [1] element of first 3
        return [item[1] for item in sorted(res)[:3]]
            
    def dfs(self,node, path, res):
        # 8. Check if node is end of the sentence
        # if so, add path to res
        if node.isEnd:
            # 9. when add to res, we also want to add hot for sorting
            res.append((node.hot,path))
        # 10. keep going if the node has child
        # until there is no more child (reached to bottom)
        for c in node.children:
            self.dfs(node.children[c], path+c,res)

    def input(self, c):
        if c != "#":
            # 5. if input is not "#" add c to self.searchTerm and do self.search each time
            self.searchTerm +=c
            return self.search()
        
        else:
            self.add(self.searchTerm, 1)
            self.searchTerm =""