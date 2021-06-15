class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # greedy
        a, b, c = False, False, False
        for t in triplets:
            if not (t[0] > target[0] or t[1] > target[1] or t[2] > target[2]):
                # else one of them exceed, no solution then
                # print(t)
                if t[0] == target[0]: 
                    a = True
                if t[1] == target[1]: 
                    b = True
                if t[2] == target[2]: 
                    c = True
        return a and b and c