class Solution0:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie, res = Trie(), 0
        for num in nums:
            trie.insert(num)
        
        for num in nums:
            node = trie.root
            res = max(res, trie.query(num))
        return res
        
class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, num):
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in p:
                p[cur] = {}
            p = p[cur]
                
    def query(self, num):
        if not self.root: 
            return -1
        p, res = self.root, 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p:
                p = p[1 - cur]
                res |= (1 << i)
            else:
                p = p[cur]
        return res


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
    
class Solution3(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trie = Trie()
        for num in nums:
            trie.insert(num)
        
        res = 0
        for num in nums:
            res = max(res, trie.search(num))
        return res

class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in node.children:
                node.children[cur] = TrieNode()
            node = node.children[cur]
    
    def search(self, num):
        res = 0
        node = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in node.children:
                node = node.children[1 - cur]
                res += (1 << i)
            else:
                node = node.children[cur]
        return res