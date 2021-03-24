'''
if cmp == 1, then we know that all nodes having the same bit value as "val" will result this digit to be 0 after xor, which are guaranteed to be smaller than "high", so we can add all of those nodes and move onto the sub-trie that have different value than "bit" (1^bit is just a fancier way to say "change 0 to 1 and change 1 to 0")
otherwise, if cmp == 0, we know all nodes that have different bit value as "val" will result something larger so we can ignore all those and only traverse the sub-trie that has the same value as "bit" (which, after xor, will result this digit to be zero)
'''

class Trie: 
    def __init__(self): 
        self.root = {}
        
    def insert(self, val): 
        node = self.root 
        for i in reversed(range(15)):
            bit = (val >> i) & 1
            if bit not in node: 
                node[bit] = {"cnt": 1} # init
            else: 
                node[bit]["cnt"] += 1 # acc
            node = node[bit]
        
    def count(self, val, high): 
        ans = 0 
        node = self.root
        for i in reversed(range(15)):
            if not node: break 
            bit = (val >> i) & 1 
            cmp = (high >> i) & 1
            if cmp: 
                # all nodes below are smaller than high
                if node.get(bit, {}): 
                    ans += node[bit]["cnt"] # update counts when < high
                node = node.get(1^bit, {}) # flip, get bigger if 
            else: 
                # all nodes below are bigger than high, just travese and dont update
                node = node.get(bit, {}) # 
        return ans 
                

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()
        
        res = 0
        for x in nums: 
            res += trie.count(x, high + 1) - trie.count(x, low) # get prefix sum
            trie.insert(x) # update prefix
        return res 