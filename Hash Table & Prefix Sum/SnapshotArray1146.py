class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot = {i: {0: 0} for i in range(length)}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snapshot[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # ["SnapshotArray","snap","snap","get","set","snap","set"]
        # [[4],[],[],[3,1],[2,4],[],[1,4]]
        # When retrieving a value (get(...) method), it will travel back to previous versions until a value for a requested index is found. 
        # If value is not found, return a default value 0.
        while snap_id > 0 and snap_id not in self.snapshot[index]:
            snap_id -= 1
        # print(self.snapshot)
        return self.snapshot[index][snap_id]

class SnapshotArray2(object):

    def __init__(self, length):
        self.nums = {}
        self.snaps = []   

    def set(self, index, val):
        self.nums[index] = val

    def snap(self):
        self.snaps.append(self.nums.copy()) # shallow copy
        return len(self.snaps) - 1

    def get(self, index, snap_id):
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        else:
            return 0


class SnapshotArray_binary_search(object):

    def __init__(self, n):
        self.A = [[[-1, 0]] for _ in xrange(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1 # binary search the snap_id
        return self.A[index][i][1]
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)