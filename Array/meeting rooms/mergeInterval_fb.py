'''

has open and closed 

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

last 2 digits is status of open & closed
if 1: closed, can merge
if 0: open, cannot merge

open close only happened on this case: [1,3,_, 1] [3,5, 1, _] => merge because both closed

https://www.1point3acres.com/bbs/thread-795819-1-1.html

input: [[1,3,1,1],[2,6,1,1],[8,10,1,1],[15,18,1,1]]
output: [[1, 6, 1, 1], [8, 10, 1, 1], [15, 18, 1, 1]]
'''

intervals = [[1,3,1,1],[2,6,1,1],[8,10,1,1],[15,18,1,1]]

intervals2 = [[1,3,1,1],[3,6,0,1],[8,10,1,1],[15,18,1,1]]

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        for s, e, s_oc, e_oc in intervals:
            # print(res)
            if not res or s > res[-1][1]:
                res.append([s, e, s_oc, e_oc])
            elif s < res[-1][1]: # [1,3] , [2, 4]
            	# overlapped
            	if e > res[-1][1]:
                	res[-1][1] = e
                	res[-1][3] = e_oc
            elif s == res[-1][1]: # [1,3] (res[-1]), [3, 5]
            	if res[-1][-1] == 1 and s_oc == 1:
            		# overlapped, so merge
            		if e > res[-1][1]:
	                	res[-1][1] = e
	                	res[-1][3] = e_oc
            	else:
            		# dont merge
            		res.append([s, e, s_oc, e_oc])
        return res

soln = Solution()
print(soln.merge(intervals))
print(soln.merge(intervals2))


