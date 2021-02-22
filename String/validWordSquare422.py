class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # Only three false conditions: too short, too long, letter not equal
        for i in range(len(words)):
            for j in range(len(words[i])):
                # too long, j >= len(words), too short, len(words[j]) <= i
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True