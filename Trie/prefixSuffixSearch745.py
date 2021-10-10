class TrieNode():
    def __init__(self):
        self.children = {}
        self.weights = []

# create two Tries, one for prefix search, 
# another one for suffix search
# then find the maximal common weight
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, i):
        node = self.root
        node.weights.append(i)
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.weights.append(i)
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.weights
        
class WordFilter1:
    # TLE in Oct 2021
    def __init__(self, words: List[str]):
        self.prefix, self.suffix = Trie(), Trie()
        i, n = 0, len(words)
        while i < n:
            w = words[i]
            self.prefix.insert(w, i)
            self.suffix.insert(w[::-1], i)
            i += 1

    def f(self, prefix: str, suffix: str) -> int:
        pre = self.prefix.search(prefix)
        suf = self.suffix.search(suffix[::-1])
        # print(pres, sufs) # find overlap, they are both increasing!

        i, j = len(pre) - 1, len(suf) - 1
        while i >= 0 and j >= 0:
            if pre[i] == suf[j]:
                return pre[i]
            elif pre[i] < suf[j]:
                j -= 1
            else:
                i -= 1
        return -1



class WordFilter2:

    def __init__(self, words: List[str]):
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        self.weights = {}
        for index, word in enumerate(words):
            prefix, suffix = '', ''
            for char in [''] + list(word):
                prefix += char
                self.prefixes[prefix].add(word)
            for char in [''] + list(word[::-1]):
                suffix += char
                self.suffixes[suffix[::-1]].add(word)
            self.weights[word] = index

    def f(self, prefix: str, suffix: str) -> int:
        weight = -1
        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            # print(self.prefixes[prefix], self.suffixes[suffix])
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight