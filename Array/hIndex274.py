class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 6,5,(3),1,0
        citations.sort(reverse=True)
        n = len(citations)
        for i in range(n):
            # print(i)
            if citations[i] < i + 1:
                return i
        return n