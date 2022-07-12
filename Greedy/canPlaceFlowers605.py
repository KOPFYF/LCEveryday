class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # greedy
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                # plant 1 in the middle
                flowerbed[i] = 1
                count += 1
        return count >= n