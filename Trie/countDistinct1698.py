class Solution:
    def countDistinct(self, s: str) -> int:
        # trie O(n^2)
        # trie, res = dict(), 0
        # for i in range(len(s)):
        #     cur = trie
        #     for j in range(i, len(s)):
        #         # for substring from i to j
        #         if s[j] not in cur: 
        #             #if current substring is not a prefix
        #             cur[s[j]] = dict()
        #             res += 1
        #         elif "#" not in cur:
        #             # if it is a prefix, but doesn't appear as a string.
        #             res += 1
        #         cur["#"] = True # to indicate that this substring exists
        #         cur = cur[s[j]]
        #     cur["#"] = True
        # return res
    
        trie, res = dict(), 0
        for i in range(len(s)):
            cur = trie
            for j in range(i,len(s)):# for substring from i to j
                if s[j] not in cur: #if current substring has not appeared previously.
                    cur[s[j]] = dict()
                    res += 1
                cur = cur[s[j]] # go to next level
            print(cur)
        return res