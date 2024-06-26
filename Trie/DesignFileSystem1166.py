class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        '''
        Creates a new path and associates a value to it if possible and returns true. 
        Returns false if 
            - the path already exists or
            - its parent path doesn't exist.
        '''
        node = self.root
        dirs = path.split('/')[1:]
        size = len(dirs)
        for i, f in enumerate(dirs):
            if f not in node.children:
                if i < size - 1:
                    return False # its parent path doesn't exist.
                else:
                    node.children[f] = TrieNode()
                    node.children[f].value = value
                    return True
            else:
                if i == size - 1:
                    return False # the path already exists
                node = node.children[f]
                      
    def get(self, path: str) -> int:
        node = self.root
        for f in path.split('/')[1:]:
            if f not in node.children:
                return -1
            node = node.children[f]
        return node.value


class TrieNode:
    def __init__(self, value):
        self.children = {}
        # self.name = name
        self.value = value

class FileSystem:

    def __init__(self):
        self.root = TrieNode(0)
        
    def createPath(self, path: str, value: int) -> bool:
        '''
        Creates a new path and associates a value to it if possible and returns true. 
        Returns false if 
            - the path already exists or
            - its parent path doesn't exist.
        '''
        node = self.root
        files = path.split('/')
        size = len(files)
        for i in range(1, size):
            file = files[i]
            if i == size - 1: 
                # can only extend in the leaf node
                if file in node.children:
                    return False # path already exists
                node.children[file] = TrieNode(value)
                return True # extend one step and return True
            else:
                if file not in node.children:
                    return False # its parent does not exist
                node = node.children[file]
            

    def get(self, path: str) -> int:
        '''
        Returns the value associated with path or returns -1 if the path doesn't exist
        '''
        node = self.root
        files = path.split('/')
        size = len(files)
        for i in range(1, size):
            file = files[i]
            if file not in node.children:
                return -1
            node = node.children[file]
        return node.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)