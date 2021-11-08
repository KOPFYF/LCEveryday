'''
Convert each interval to two pairs: <value, start/end> and put them into a 2N vector

Sort the created vector based on the value, where "end" values comes before the "start" ones
Loop through the vector and increment a counter when finding a "start" pair, 
decrement it when finding a "end" pair. Keep track of the value when the counter has is maximum.
Return the value when counter was max

Time complexity: O(NlogN)
Space complexity: O(N)

'''

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, s, e in trips:
            events.append((s, num))
            events.append((e, -num))
        
        events.sort()
        
        cnt = 0
        for se, diff in events:
            cnt += diff
            if cnt > capacity:
                return False
        return True


# https://leetcode.com/discuss/interview-question/396248/Facebook-or-Phone-Screen-or-Point-in-max-overlapping-interva&#8205;&#8205;&#8205;&#8204;&#8204;&#8204;&#8205;&#8204;&#8204;&#8205;&#8204;&#8204;&#8205;&#8205;&#8204;&#8204;&#8204;&#8205;ls

'''
Given number M and N intervals in the form [a, b] (inclusive) where for every interval -M <= a <= b <= M, 
create a program that returns a point where the maximum number of intervals overlap.

Example:

M: 10
N: 4
Intervals:
[-3, 5]
[0, 2]
[8, 10]
[6, 7]
A correct answer would be either 0 ,1 or 2 since those points are found where 2 intervals overlap 
and 2 is the maximum number of overlapping intervals.
'''

intervals = [[-3, 5], [0, 2], [8, 10], [6, 7]]

def sweep_maxnum(intervals):
    events = []
    for s, e in intervals:
        events.append((s, 1))
        events.append((e, -1))

    events.sort() # O(nlogn)
    cnt = 0
    max_cnt = 0
    res = None

    for se, diff in events:
        cnt += diff
        if cnt > max_cnt:
            res = se 
            max_cnt = cnt 
    return res

print(sweep_maxnum(intervals)) # return 0















