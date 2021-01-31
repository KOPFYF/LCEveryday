class Solution1(object):
    def getSkyline(self, buildings):
        # 不难发现这些关键点的特征是：竖直线上轮廓升高或者降低的终点
        # 所以核心思路是：从左至右遍历建筑物，记录当前的最高轮廓，如果产生变化则记录一个关键点
        
        # 首先记录构造一个建筑物的两种关键事件
        # 第一种是轮廓升高事件(L, -H)、第二种是轮廓降低事件(R, 0)
        # 轮廓升高事件(L, -H, R)中的R用于后面的最小堆
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})

        # 先根据L从小到大排序、再根据H从大到小排序(记录为-H的原因)
        # 这是因为我们要维护一个堆保存当前最高的轮廓
        events.sort()

        # 保存返回结果
        res = [[0, 0]]
        
        # 最小堆，保存当前最高的轮廓(-H, R)，用-H转换为最大堆，R的作用是记录该轮廓的有效长度
        live = [(0, float("inf"))]

        # 从左至右遍历关键事件
        for L, negH, R in events:
            
            # 如果是轮廓升高事件，记录到最小堆中
            if negH: 
                heappush(live, (negH, R))
            
            # 获取当前最高轮廓
            # 根据当前遍历的位置L，判断最高轮廓是否有效
            # 如果无效则剔除，让次高的轮廓浮到堆顶，继续判断
            while live[0][1] <= L: 
                heappop(live)
            
            # 如果当前的最高轮廓发生了变化，则记录一个关键点
            if res[-1][1] != -live[0][0]:
                res += [ [L, -live[0][0]] ]
        return res[1:]


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