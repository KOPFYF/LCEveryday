'''
bitmask or set operation will do
return the indices in increasing order.
'''
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        d = {i: set(c) for i, c in enumerate(favoriteCompanies)}
        # print(d)
        res, n = [], len(favoriteCompanies)
        for i in range(n):
            flag = True
            for j in range(n):
                if i == j:
                    continue
                if not d[i] - d[j]: # i is subset of j
                # if d[i].issubset(d[j]):
                    flag = False
                    break
            if flag:
                # i is not a subset of anyone
                res.append(i)
        return res