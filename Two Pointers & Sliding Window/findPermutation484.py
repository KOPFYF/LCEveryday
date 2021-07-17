'''
For example, given IDIIDD we start with sorted sequence 1234567
IDIIDD
1234567 // sorted
1(32)4(765) // answer
i = 1, j = 2
i = 4, j = 6

Then for each k continuous D starting at index i we need to reverse [i, i+k] portion of the sorted sequence.
'''
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = []
        # indicates the value of the last element that is put in the ans array
        prev = 0
        res = [0] * (len(s) + 1)
        for i, ch in enumerate(s + "I"):
            if ch == "I":
                prev = prev + 1
                res[i] = prev
                while stack:
                    prev += 1
                    res[stack.pop()] = prev
            else:
                stack.append(i)
            # print(ch, ans, stack)
        return res
    
        def reverse(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        i, n = 0, len(s)
        arr = list(range(1, n + 2))

        while i < n:
            if s[i] == 'D':
                j = i
                while j < n and s[j] == 'D': # move i as right pointer
                    j += 1
                # print(i, j)
                reverse(arr, i, j)
                i = j
            i += 1
        return arr
                
        