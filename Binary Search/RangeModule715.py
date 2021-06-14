class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left, right):
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