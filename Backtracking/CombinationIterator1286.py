class CombinationIterator:
    '''
    bit mask, 2^15
    Eg: "abc", 2
    We start with "111" which is 7. Run a loop over 0 to 7 both inclusive. The possible values with 2 set bits are ["011", "101", "110"]
    '''

    def __init__(self, characters: str, combinationLength: int):
        # sorted & distinct, so permutation would gurantee the lexicographical order.
        self.characters = characters 
        self.n = combinationLength
        self.i = 0
        self.res = []
        self.permute('', 0)


    def permute(self, s, start):
        if len(s) == self.n:
            self.res.append(s)
            return
        for i in range(start, len(self.characters)):
            self.permute(s + self.characters[i], i + 1) # take char[i]


    def next(self) -> str:
        res = self.res[self.i]
        self.i += 1
        # print(self.res)
        return res


    def hasNext(self) -> bool:
        return self.i < len(self.res)
        
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()