class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ''

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
    
    def _insert(self, path):
        node = self.root
        for f in path.split('/')[1:]:
            if f not in node.children:
                # If the middle directories in the path do not exist, you should create them as well.
                node.children[f] = TrieNode()
            node = node.children[f]
        return node
    
    def _search(self, path):
        node = self.root
        for f in path.split('/')[1:]:
            if f not in node.children:
                return node
            node = node.children[f]
        return node
        
    def ls(self, path: str) -> List[str]:
        '''
        If path is a file path, returns a list that only contains this file's name.
        If path is a directory path, returns the list of file and directory names in this directory.
        '''
        files = [path.split('/')[-1]] # get last file
        node = self._search(path)
        # If path is a file path
        if node.word: # node.word is not empty only if it's a file(leaf node with content), not a dir
            return files
        # If path is a directory path, return all children
        return sorted(node.children.keys())
        
    def mkdir(self, path: str) -> None:
        self._insert(path)
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._insert(filePath)
        node.word += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._search(filePath)
        return node.word


##########################################################


class TrieNode:
    def __init__(self):
        self.children = {}
    
    def setdefault(self, token):
        return self.children.setdefault(token, TrieNode())
    
    def get(self, token):
        return self.children.get(token, None)

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        self.file_paths = defaultdict(str) # mapping filepaths to the str content in their files
        
    def ls(self, path: str) -> List[str]:
        if path in self.file_paths:
            return path.split('/')[-1:] # get rid of empty string
        cur = self.root
        for token in path.split('/'):
            print('ls:', token, path.split('/'))
            if cur and token: # token could be empty, for example, '/' => ['', '']
                cur = cur.get(token) # go down the tree
        
        return sorted(cur.children.keys()) if cur else [] # if path not valid, return []
        
    def mkdir(self, path: str) -> None:
        cur = self.root
        for token in path.split('/'):
            print('mkdir:', token, path.split('/'))
            if token:
                cur = cur.setdefault(token)
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        # appends the given content to original content
        self.file_paths[filePath] += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.file_paths[filePath]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)