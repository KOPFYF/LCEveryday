'''
If k = 1, only rotations of s are possible, and the answer is the lexicographically smallest rotation.

If k > 1, any permutation of s is possible, and the answer is the letters of s written in lexicographic order.

I think this works similar to how bubble sort works. In case of K == 1, we cannot switch two elements, so sorting is impossible. In case of K >= 2, theoretically, we can swap two unsorted elements by switching a[0] and a[1] and send them to the end of the list. Then, we rotate the array so that the array is arranged as a[1], a[0], a[2], a[3] ... , which is equivalent to completion of the first step of a bubble sort. Now, using this protocol, we can basically sort the alphabets if K >= 2.
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # O(n) / O(n)
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        else:
            return ''.join(sorted(s))