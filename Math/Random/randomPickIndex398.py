import random

class Solution0:
    # reservoir sampling
    '''
    {1,2,3,3,3} with target 3, you want to select 2,3,4 with a probability of 1/3 each.
    
    2 : It's probability of selection is 1 * (1/2) * (2/3) = 1/3
    3 : It's probability of selection is (1/2) * (2/3) = 1/3
    4 : It's probability of selection is just 1/3

    So they are each randomly selected

    '''
    def __init__(self, nums):
        self.nums = nums
        
    def pick(self, target):
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res


class Solution1:
    # hashmap
    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for i, num in enumerate(nums):
            self.d[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])


class Solution2:
    # list
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        
    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])