class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # a) At each step, we choose the element with highest freq (a, b) where b is the element, to append to result.
        # b) Now that b is chosen. We cant choose b for the next loop. So we dont add b with decremented value count immediately into the heap. Rather we store it in prev_a, prev_b variables.
        # c) Before we update our prev_a, prev_b variables as mentioned in step 2, we know that whatever prev_a, prev_b contains, has become eligible for next loop selection. so we add that back in the heap.
        res, c = [], Counter(S)
        pq = [(-v, k) for k, v in c.items()] # max heap with freq. count
        heapq.heapify(pq)
        
        p_a, p_b = 0, '' # a tuple of previous (-value, char)
        while pq:
            a, b = heapq.heappop(pq)
            res += [b]
            if p_a < 0: # push back the last item
                heapq.heappush(pq, (p_a, p_b))
            a += 1 # we use once, so dec the freq by 1
            p_a, p_b = a, b # loop
        # print(res, pq)    
        res = ''.join(res)
        if len(res) != len(S): return "" 
        return res

        # soln 2
        if len(pq) <= 1:
            return ""

        result = []
        while len(pq) >= 2:
            (val1, key1) = heapq.heappop(pq)
            (val2, key2) = heapq.heappop(pq)
            result.append(key1)
            result.append(key2)
            if val1 + 1: # if val != -1, dec freq by 1, meaningless to push 0
                heapq.heappush(pq, (val1+1, key1))
            if val2 + 1:   
                heapq.heappush(pq, (val2+1, key2))

        while pq:
            val, key = heapq.heappop(pq)
            if val >= 0:
                continue
            if key == result[-1]:
                # this means we have something like h = [(2, "a")] 
                # which means there is no escape from repeating same char in text
                return ""
            result.append(key)
            heapq.heappush(pq, (val+1, key))
        
        return ''.join(result)
            
            