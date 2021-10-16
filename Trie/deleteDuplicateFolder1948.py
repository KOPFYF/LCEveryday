class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.deleted = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        def serialize(node, seen):
            # return a string of all children under current node
            if not node.children:
                return ''
            keys = []
            for ch, child_node in node.children.items():
                keys.append(ch + ':' + serialize(child_node, seen))
            key = "(" + "".join(keys) + ')'
            seen[key].append(node) # key is tree-string, value is a list of nodes
            return key
        
        def dfs(node, path, out):
            # dfs to recrusively pruning
            for ch, child_node in node.children.items():
                if not child_node.deleted:
                    out.append(path + [ch])
                    dfs(child_node, path + [ch], out)
        
        trie, seen = Trie(), defaultdict(list)
        # build trie tree
        for path in sorted(paths):
            trie.insert(path)
        
        # Find duplicated subtrees
        serialize(trie.root, seen)
        print(seen)
        print(seen.keys()) # dict_keys(['(b:)', '(a:)', '(a:(b:)c:(b:)d:(a:))'])
        
        for nodes in seen.values():
            if len(nodes) >= 2: # find a dup
                for node in nodes:
                    node.deleted = True # marked as to be delete
        
        res = []
        dfs(trie.root, [], res)
        return res
        
            
        
        
        
        
        