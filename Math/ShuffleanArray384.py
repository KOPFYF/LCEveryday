class Solution:
    '''
    randint(a, b)
    Return a random integer N such that a <= N <= b. 
    Alias for randrange(a, b+1).
    '''

    def __init__(self, nums: List[int]):
        self.org = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.org

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.org[:]
        for i in range(len(self.org)-1, 0, -1):
            j = random.randrange(0, i + 1)
            res[i], res[j] = res[j], res[i]
        return res