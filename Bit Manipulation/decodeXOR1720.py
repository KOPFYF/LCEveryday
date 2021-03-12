class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for x in encoded:
            # print(x, first, x ^ first)
            nxt = x ^ first
            res.append(nxt)
            first = nxt
        return res