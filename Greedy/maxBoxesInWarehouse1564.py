class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # greedy, try smallest box, O(n + mlogm) / O(m) -- for sorting
        boxes.sort()
        # preprocess the warehouse as there is some bottleneck in the middle
        # after this warehouse will be non-increasing
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i - 1], warehouse[i])
        count = 0
        for w in reversed(warehouse):
            if count < len(boxes) and boxes[count] <= w:
                count += 1
        return count


class Solution1:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        i = 0 # index of box
        count = 0
        boxes.sort(reverse = True)

        for w in warehouse:
            # Iterate through boxes from largest to smallest
            # Discard boxes that doesn't fit in the current warehouse
            while i < len(boxes) and boxes[i] > w:
                i += 1
            if i == len(boxes):
                return count
            count += 1
            i += 1

        return count