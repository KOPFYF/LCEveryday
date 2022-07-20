'''
Intuition:

Since Ls and Rs can ONLY move to empty spaces and can NOT swap, the sequences containing all Ls and Rs and only Ls and Rs of start and target must be same;
Since Ls and Rs can move to left and right only respectively, all positions of Ls in start must be no less than the corresponding ones in target, and all positions of Rs in start must be no greater than the corresponding ones in target.

Based on the above conclusion we can implement an algorithm as follows:

Algorithm:

1. Check if start and target are same if without _'s;
2. Check if all positions of L's in start are no less than those in target;
3. Check if all positions of R's in start are no greater than those in target;
4. If all above 3 are yes, return true; otherwise return false.
'''
class Solution:
    def canChange(self, s: str, t: str) -> bool:
        if s.replace('_', '') != t.replace('_', ''):
            return False
        i, j, n = 0, 0, len(s)
        while i < n and j < n:
            while i < n and s[i] == '_':
                i += 1
            while j < n and t[j] == '_':
                j += 1
            if i < n and j < n and (s[i] == 'L' and i < j or s[i] == 'R' and i > j):
                return False
            i += 1
            j += 1
        return True
        
        