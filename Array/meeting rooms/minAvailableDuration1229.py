class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:  
        # 2 ptrs
        slots1.sort()
        slots2.sort()
        n1, n2 = len(slots1), len(slots2)
        i, j = 0, 0
        while i < n1 and j < n2:
            s = max(slots1[i][0], slots2[j][0])
            e = min(slots1[i][1], slots2[j][1])
            if s + duration <= e:
                return [s, s + duration]
            elif slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
    
        # Put both slots1 and slots2 into PriorityQueue/heapq 
        # (first filter slots shorter than duration), sort by starting time;
        # Pop out the slots one by one, comparing every consective two to check if having duration time in common.
        s = list(filter(lambda slot: slot[1] - slot[0] >= duration, slots1 + slots2))
        # s = [slot for slot in slots1+slots2 if slot[1] - slot[0] >= duration]
        # print(s) # just filter out short intervals
        heapq.heapify(s)
        # print(s) # [[0, 15], [10, 50], [140, 210], [60, 120], [60, 70]]
        while len(s) > 1:
            if heapq.heappop(s)[1] >= s[0][0] + duration:
                return [s[0][0], s[0][0] + duration] 
        return [] 