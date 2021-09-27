import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # https://stackoverflow.com/questions/33701160/python-heapq-difference-between-heappushpop-and-heapreplace
        # heapreplace(a, x) returns the smallest value originally in a regardless of the value of x
        max_heap = []
        for count, token in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if count: heapq.heappush(max_heap, (count, token))
        result = []
        while max_heap:
            count, token = heapq.heappop(max_heap) # char1
            if len(result) > 1 and result[-2] == result[-1] == token:
                if not max_heap: # no char2, return directly
                    break
                # pop out char2, then push back char1
                count, token = heapq.heapreplace(max_heap, (count, token))
            result.append(token)
            if count + 1: 
                heapq.heappush(max_heap, (count + 1, token)) # update and push char2
        return ''.join(result)
        
        
        # heap simulation + greedy
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, 'a'))
        if b != 0:
            heappush(max_heap, (-b, 'b'))
        if c != 0:
            heappush(max_heap, (-c, 'c'))
        s = []
        while max_heap:
            first, char1 = heappop(max_heap) # char with most rest numbers
            if len(s) >= 2 and s[-1] == s[-2] == char1: # check whether this char is the same with previous two
                if not max_heap: # if there is no other choice, just return
                    return ''.join(s)
                second, char2 = heappop(max_heap) # char with second most rest numbers
                s.append(char2)
                second += 1 # count minus one, because the second here is negative, thus add 1
                if second != 0: # only if there is rest number count, add it back to heap
                    heappush(max_heap, (second, char2))
                heappush(max_heap, (first, char1)) # also need to put this part back to heap
                continue
			
			#  situation that this char can be directly added to answer
            s.append(char1)
            first += 1
            if first != 0:
                heappush(max_heap, (first, char1))
        return ''.join(s)
        