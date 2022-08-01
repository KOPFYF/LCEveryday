class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(NK)/O(1)
        if not strs:
            return ""
        
        shortest = min(strs, key=len)
        # print(shortest)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch: # greedy
                    return shortest[:i] # when i=0, return ""
        return shortest 