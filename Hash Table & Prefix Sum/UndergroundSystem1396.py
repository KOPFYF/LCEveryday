class UndergroundSystem:

    def __init__(self):
        self.user = defaultdict(list)
        self.dest = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # for each start-end pair, append the user time interval
        startStation, prevT = self.user[id]
        self.dest[(startStation, stationName)].append(t - prevT)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = self.dest[(startStation, endStation)]
        return float(sum(time)/len(time)) if time else 0