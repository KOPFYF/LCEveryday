class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1 <= strs.length <= 104
        def str2tuple(s):
            # O(len(s)) / O(26)
            res = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                res[idx] += 1
            return tuple(res)
        
        
        d = defaultdict(list)
        # O(len(strs) len(s)) / O(26 * len(strs))
        for s in strs:
            d[str2tuple(s)].append(s)
        # print(d)
        
        ans = []
        for v in d.values():
            ans.append(v)
        return ans


        d = {}
        for w in strs:
            key = tuple(sorted(w)) # key is immutable, so turn it intp tuple
            d[key] = d.get(key, []) + [w]
        return d.values()
    
        hmap = collections.defaultdict(list)
        for st in strs:
            array = [0] * 26
            for l in st:
                array[ord(l) - ord('a')] += 1
            hmap[tuple(array)].append(st)
        return hmap.values()