class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = defaultdict(int)
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.s[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.s:
            cmp = value - num
            if cmp in self.s and (cmp != num or self.s[cmp] > 1):
                return True
        return False