import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.idxs = collections.defaultdict(set) # for each unique value, set stores all indexes
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        self.idxs[val].add(len(self.nums) - 1)
        return len(self.idxs[val]) == 1 # set has only 1 index
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.idxs[val]:
            idx = self.idxs[val].pop() # 
            tmp = self.nums[-1] # switch the last item with val
            self.nums[idx] = tmp
            self.idxs[tmp].add(idx)
            self.idxs[tmp].discard(len(self.nums) - 1)
            self.nums.pop()
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.nums)