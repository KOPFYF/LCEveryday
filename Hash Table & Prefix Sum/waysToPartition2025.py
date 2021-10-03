'''
hints:
1. A pivot point splits the array into equal prefix and suffix. If no change is made to the array, the goal is to find the number of pivot p such that prefix[p-1] == suffix[p].

2. Consider how prefix and suffix will change when we change a number nums[i] to k.

3. When sweeping through each element, can you find the total number of pivots where the difference of prefix and suffix happens to equal to the changes of k-nums[i].

https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/discuss/1498999/C%2B%2B-O(n)

Requirements

We need count of indexes i, such that nums[0] + ... + nums[i-1] == nums[i] ... nums[n-1], that is prefixSum[i-1] = SuffixSum[i].
We are also allowed to change the an element to 'K'.
We need to return max possible count of such indexes.
Thought Process

How can we find the count of pivots, if we are not allowed to change any value?
We can iterate over prefixSum array, and count all indexes where pref[i] == suff[i+1].
Now suppose we are allowed to change an element, say nums[j] to value K. How will it change the array prefixSum and suffixSum?
Let d be the increase in jth element => d = K - nums[j]
We can easily see, all values from pref[ j ] to pref[n-1] will also increase by d, and all values from suff[ j ] to suff[ 0 ], will also increase by d.
So, if we had the count of all indexes i, such that:
if i < j, then pref[ i ] - suff[ i + 1] = d, in original array i.e. without changing j's value

Because, suffix sum from 0 to j is increased by d.
Thus this difference will now become 0.
Hence, i will become a pivot point.
if i >= j, then pref [ i ] - suff[ i+1 ] = -d, in original array i.e. without changing j's value

Because, prefix sum from j to n-1 is increased by d.
Thus this difference will now become 0.
Hence, i will become a pivot point.
Algorithm & Code

As seen in the thought process, difference between prefSum[ i ] - suffSum[ i+1 ] is the thing which actually matters.
Thus, we maintain two hash maps, left & right, which store the count of differences.
left stores the count of difference for j < i && right stores for j >= i.
Intially, when no elements is changed, left is empty, right will contain all the differences.
Now, whenever we change the element i, then we check count of difference d = k - nums[i] in left and -d in right.
Then, we transfer the current element from, hashMap right to hashMap left.


'''

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix, suffix = [0] * n, [0] * n
        prefix[0], suffix[-1] = nums[0], nums[-1]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
            suffix[n-i-1] = suffix[n-i] + nums[n-i-1]
        
        left, right = Counter(), Counter()
        
        # Intially, when no elements is changed, left is empty, right will contain all the differences.
        for i in range(n - 1):
            right[prefix[i] - suffix[i+1]] += 1

        # unchanged
        res = right[0] 
        
        # find the number of pivot indexes when nums[i] is changed to k
        for i in range(n):
            cur, diff = 0, k - nums[i]
            cur += left[diff]
            cur += right[-diff]
            res = max(res, cur)
            
            # transfer the current element from right to left
            if i < n - 1:
                dd = prefix[i] - suffix[i+1]
                left[dd] += 1
                right[dd] -= 1
                # if right[dd] == 0:
                #     del right[dd]
        return res

'''
Explanation

For each pivot p, 1 <= p <= n-1, we can test whether it is a valid partition point by checking whether sum(nums[:p]) == sum(nums[p:]), which can be determined in constant time after computing prefix sums.

If a pivot p is not valid, we compute gap[p] = sum(nums[p:]) - sum(nums[:p]). This gap[p] is how much we need to add to an element strictly before index p, or subtract from an element at or after index p, in order to make p a valid pivot.

Now, for each element nums[i], find the number of valid pivots in the new array after changing nums[i] to k, or in other words, adding k-nums[i] at index i.

This number is the count of indices p >= i, with gap[p] == k-nums[i], plus the number of indices 1 <= p < i with - gap[p] == k-nums[i].

Use two dictionaries (for earlier gap counts and later gap counts) plus a prefix sum array, and update the dictionaries as we traverse.

Complexity

Time complexity: O(n), Space complexity O(n)

'''

class Solution1:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        prefix_sums = list(accumulate(nums))
        total_sum = prefix_sums[-1]
        best = 0
        if total_sum % 2 == 0:
            best = prefix_sums[:-1].count(total_sum // 2)  # If no change

        before_counts = Counter(total_sum - 2 * prefix_sum
                                for prefix_sum in prefix_sums[:-1])
        after_counts = Counter()

        best = max(best, before_counts[k - nums[0]])  # If we change first

        for prefix, x in zip(prefix_sums, nums[1:]):
            gap = total_sum - 2 * prefix
            before_counts[gap] -= 1
            after_counts[-gap] += 1

            best = max(best, before_counts[k - x] + after_counts[k - x])

        return best
                