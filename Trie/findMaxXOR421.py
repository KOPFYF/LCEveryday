class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None

class Solution_Trie:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # build trie first
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                if num & 1 << i:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
        # loop each byte of num
        res = 0
        for num in nums:
            node = root
            maxi = 0
            for i in range(31, -1, -1):
                if num & 1 << i and node.zero: # find a 1, go to node.zero
                    maxi += 1 << i
                    node = node.zero
                elif not num & 1 <<i and node.one: # find a 0, go to node.one
                    maxi += 1 << i
                    node = node.one
                else: # no result for the current level
                    node = node.one or node.zero
            res = max(res, maxi) # update for each num
        return res

class Solution1:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://www.youtube.com/watch?v=ZHtZfkAcPKc&t=54s
        """
        # Build the answer bit by bit from left to right
        # a ^ b = res => a ^ res = b
        res = 0
        for i in range(31, -1, -1):
            res <<= 1 
            prefixes = {num >> i for num in nums} # get prefix(bits) for each num
            nxt = res + 1 # get next biggest mask based on last round res
            if any(nxt ^ p in prefixes for p in prefixes):
                 res = nxt
            # res += any(nxt ^ p in prefixes for p in prefixes)
            # print(bin(res)[2:], [bin(pre)[2:] for pre in prefixes])
        return res
    
class Solution2:
    def findMaximumXOR(self, nums):    
        res, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            found = set([num & mask for num in nums])
            # print([bin(pre)[2:] for pre in found])
                
            start = res | 1 << i
            for pref in found:
                if start ^ pref in found:
                    res = start
                    break
         
        return res
    