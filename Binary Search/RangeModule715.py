class RangeModule:
    '''
    Odd positions lie between ranges. The way to think about this is that ranges are pairs. 
    If you need to insert in an odd place, it always lies within range. 
    I think about it as if it lies within a range, it is consumed/superseded by that range. 
    Hence you do not need to add that.

    [1,3,9,11]

    [1,3), [9,11), now we insert [4,6), bisect(4) return 2, even, so safe to insert, 6 is the same
    if insert[3, 6), bisect(3) return 1, odd, so overlapped, we dont add it to final
    now it becoms [1,6,9,11] (insert 6 only), 3 is removed


    '''

    def __init__(self):
        self.track = []

    def addRange(self, left, right):
        # If the index is even, it means that it is currently outside the range of start and end indexes being tracked
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
			
        self.track[start:end] = subtrack

    def removeRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
			
        self.track[start:end] = subtrack
		
    def queryRange(self, left, right):
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)
		
        return start == end and start % 2 == 1