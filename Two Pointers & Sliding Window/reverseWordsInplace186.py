class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 2 ptrs O(n)/O(1)
        def reverse_words(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        reverse_words(0, len(s) - 1)
        
        i = 0
        for j, ch in enumerate(s + [" "]):
            if ch == " ":
                reverse_words(i, j - 1)
                i = j + 1