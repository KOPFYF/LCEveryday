class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        hcuts = [0] + horizontalCuts + [h]
        vcuts = [0] + verticalCuts + [w]
        dh, dv = 0, 0
        
        for h1, h2 in zip(hcuts, hcuts[1:]):
            dh = max(dh, h2 - h1)
        
        for v1, v2 in zip(vcuts, vcuts[1:]):
            dv = max(dv, v2 - v1)
        
        print(dh, dv)
            
        return dh * dv % (10**9 + 7)