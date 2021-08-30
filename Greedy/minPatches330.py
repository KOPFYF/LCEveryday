'''
https://leetcode.com/problems/patching-array/discuss/280183/Detailed-Explanation-with-Example

例子（Example）

[1,2,3,5,10,50,70], n=100

Seeing 1, we know [1,1] can be covered
Seeing 2, we know [1,3] can be covered
Similarly for 3, [1,6] can be covered
for 5, [1,11] can be covered
for 10, [1, 21] can be covered
for 50, however, we have to add a patch, if the patch is 1, the range can be extended to [1, 22], if the patch is 2, the range can be extended to [1, 23]...From the observation we know in order to extend the range as longer as possible, we need to add 22, so that we get [1,43]. Why not add 23? Because [1,2,3,5,10,23] can NOT cover 22!
[1,43] does not cover 50 yet. Following a similar way of thinking, we know this time we need to add 44, extending the range to [1, 87]
for 70, it's already in [1,87], add 70 would extend the range to [1,157]
157 > 100, done
In conclusion, we need 2 patches, i.e., 22 and 44.
So the key point is if the current range is [1,m], and the current number > m, we need to add m+1 as a patch, to extend the range to [1, 2m+1].


[1,2,3,5,10,50,70], n=100

看到第一个数1，我们知道[1,1]可以被覆盖
看到第二个数2，我们知道[1,3]可以被覆盖
3同理，[1,6]可以被覆盖
5同理，[1,11]可以被覆盖
10同理，[1,21]可以被覆盖
现在到50，发现不得不打补丁了，如果打补丁1，可以扩展为[1,22]，如果打补丁2，可以扩展为[1,23]...可见，要得到最大的范围，应该打的补丁是22，这样能得到[1,43]，为什么不能打补丁23呢？因为[1,2,3,5,10,23]得不到22！
[1,43]还是没有覆盖50，按照类似的逻辑，这次应该打的补丁是44，将范围扩充到[1,87]
最后到70，在[1,87]内，范围被扩充到[1,157]
157 > 100，结束
综上，一共要2个补丁，即22和44
所以，题目的要点在于，如果当前的范围是[1,m]，且当前的数字num > m，我们应该打补丁m+1，使得范围扩充到[1，2m+1]。
'''

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # greedy O(n)
        # goal: to cover range [1, n]
        cnt, patch, m = 0, 0, len(nums)
        i = 0
        while patch < n:
            if i < m and patch + 1 >= nums[i]:
                patch += nums[i]
                i += 1
            else:
                # if the current range is [1,m], and the current number > m, we need to add m+1 as a patch, to extend the range to [1, 2m+1]
                cnt += 1
                patch = 2 * patch + 1
            '''
            print(patch)
            Bound   +   nums[i] or patch
            1       +   2
            3       +   3
            6       +   5
            11      +   10
            21      +   (22) -- patch 1
            43      +   (44) -- pathc 2
            87      +   70
            137     >   100, done!
            '''
        return cnt