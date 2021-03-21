'''
I am using a kind of greedy method. runs build a map between tail number and the current run length. For example, for a consecutive seq 3,4,5, the key(tail number) is 5 and length is 3.

The problem is there might be multiple sub seqs which all end with the same number, but have different length. like we have another subseq 4,5. So there are two entries in the value part of 5: runs: {5: [3,2]}

so, when we met a new number 6, we want to merge it into existing subseqs. Which one should we use? Intuitively, if we pick up the shorter one and append the new number into that, we are more likely to make sure all the seqs are longer than 3. So I use a PriorityQueue to store these length.
'''
import collections
import heapq

class Solution:
    def isPossible(self, nums):
        # greedy + heap
        runs = collections.defaultdict(list) 
        for num in nums:
            
            # if found num-1, inc length by 1, else pop out 0 and restart
            # l = heapq.heappop(runs.get(num - 1, [0])) + 1 # shorter
            if num - 1 in runs:
                l = heapq.heappop(runs[num - 1]) + 1
            else:
                l = 1

            # print(runs, l, num)
            if len(runs[num - 1]) == 0:
                del runs[num - 1]
            heapq.heappush(runs[num], l) # update current num's length
        
        print(nums, runs) # defaultdict(<class 'list'>, {5: [3, 5]})
        for num, arr in runs.items():
            if len(arr) > 0 and min(arr) < 3:
                return False
        return True

A = [1,2,3,3,4,4,5,5]
B = [1,2,3,3,4]
soln = Solution()
print(soln.isPossible(A))
print(soln.isPossible(B))


class Solution2:
    # https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/C%2B%2BPython-Esay-Understand-Solution
    def isPossible(self, A):
        left = collections.Counter(A)
        end = collections.Counter()
        for i in A:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True