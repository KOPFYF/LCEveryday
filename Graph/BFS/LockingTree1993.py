class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = defaultdict(list)
        self.locked = [None] * len(parent)
        for i, p in enumerate(parent):
            if p != -1:
                self.children[p].append(i)
        
    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num]:
            self.locked[num] = user
            return True
        return False
        
    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = None
            return True
        return False
        
    def upgrade(self, num: int, user: int) -> bool:
        # traverse ancestors
        p = num
        while p != -1:
            if self.locked[p]:
                return False
            p = self.parent[p]
            
        # traverse ancestors
        cnt, bfs = 0, deque([num])
        while bfs:
            node = bfs.popleft()
            if self.locked[node]:
                cnt += 1
                self.locked[node] = None
            bfs += self.children[node]
        
        if cnt > 0:
            self.locked[num] = user
        return cnt > 0
            
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)