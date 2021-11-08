class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # [2,4,4,8]
        #.   *.  *, remove * and return [2,4]
        cnt = Counter(changed)
        if cnt[0] % 2:
            return []
        for x in sorted(cnt.keys()):
            if cnt[x] > cnt[2 * x]:
                return []
            if x != 0:
                cnt[2*x] -= cnt[x]
            else:
                cnt[x] = cnt[x] //  2 # corner case 0
        # print(cnt.keys(), list(cnt.elements()))
        return list(cnt.elements())
        
        
        arr = sorted(changed)
        dq = deque([])
        res = []
        for a in arr:
            if dq and a == dq[0]:
                dq.popleft()
            else:
                dq.append(2*a)
                res.append(a)
            print(dq)
        
        if dq:
            return []
        return res
    
    

            
        