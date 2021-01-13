class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # BFS
        boxes = set(initialBoxes) # visited box
        bfs = [i for i in boxes if status[i]] 
        for i in bfs:
            for j in containedBoxes[i]:
                # append all boxs we can visited
                boxes.add(j)
                if status[j]:
                    bfs.append(j)
            for j in keys[i]:
                # append all keys we have
                if status[j] == 0 and j in boxes:
                    # status = 0 but we can open with key
                    bfs.append(j)
                status[j] = 1 # update status w/keys
        # count the total number of candies after open all boxes.
        return sum(candies[i] for i in bfs)