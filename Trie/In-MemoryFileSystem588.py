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