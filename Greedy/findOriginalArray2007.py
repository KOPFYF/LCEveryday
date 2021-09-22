class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # delete (cur min value, 2*min) each time
        # heap
        cnt = collections.Counter(changed)
        heapq.heapify(changed)
        res = []
        while changed:
            min_ = heapq.heappop(changed)
            # check if (min_, 2*min_) exist in dict
            if cnt[min_] == 0:
                continue
            if cnt[min_*2] == 0:
                return []
            
            res.append(min_)
            # 0 is corner case, for example this testcase will fail: [0]
            if min_ == 0 and cnt[min_] <= 1:
                return []
            cnt[min_] -= 1
            cnt[min_*2] -= 1
        
        return res