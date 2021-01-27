class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # max heap
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()
        # print(events)
        # [(2, -10, 9), (3, -15, 7), (5, -12, 12), (7, 0, 0), (9, 0, 0), (12, 0, 0), (15, -10, 20), (19, -8, 24), (20, 0, 0), (24, 0, 0)]
        
        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos: 
                heappop(live)
            if negH: 
                heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [ [pos, -live[0][0]] ]
            # # print(live, res)
            # [(-10, 9), (0, inf)] * [[0, 0], [2, 10]]
            # [(-15, 7), (0, inf), (-10, 9)] * [[0, 0], [2, 10], [3, 15]]
            # [(-15, 7), (-12, 12), (-10, 9), (0, inf)] * [[0, 0], [2, 10], [3, 15]]
            # [(-12, 12), (0, inf), (-10, 9)] * [[0, 0], [2, 10], [3, 15], [7, 12]]
            # [(-12, 12), (0, inf), (-10, 9)] * [[0, 0], [2, 10], [3, 15], [7, 12]]
            # [(0, inf)] * [[0, 0], [2, 10], [3, 15], [7, 12], [12, 0]]
            # [(-10, 20), (0, inf)] * [[0, 0], [2, 10], [3, 15], [7, 12], [12, 0], [15, 10]]
            # [(-10, 20), (0, inf), (-8, 24)] * [[0, 0], [2, 10], [3, 15], [7, 12], [12, 0], [15, 10]]
            # [(-8, 24), (0, inf)] * [[0, 0], [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8]]
            # [(0, inf)] * [[0, 0], [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        return res[1:]