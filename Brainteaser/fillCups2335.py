'''
Explanation
It's a brain-teaser.

Necessary conditions (lower bound)

res >= max(A)
Because each time,
one type can reduce at most 1 cup,
so the final result is bigger or equal to max(A)

res >= ceil(sum(A) / 2)
Because each time,
we can fill up to 2 cups,
so the final result is bigger or equal to ceil(sum(A) / 2)

'''
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # brain-teaser
        return max(max(amount), (sum(amount) + 1) // 2)
        
        # maxheap
        pq = [-q for q in amount if q != 0]
        heapq.heapify(pq)
        ret = 0
        
        while len(pq) > 1:
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)
            first += 1
            second += 1
            ret += 1
            if first:
                heapq.heappush(pq, first)
            if second:
                heapq.heappush(pq, second)

        if pq:
            return ret - pq[0]
        else:
            return ret