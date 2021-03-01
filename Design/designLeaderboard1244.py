class Leaderboard:

    def __init__(self):
        self.A = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.A[playerId] += score

    def top(self, K: int) -> int:
        vs = list(self.A.values())
        vs.sort(reverse=1)
        return sum(vs[:K])

    def reset(self, playerId: int) -> None:
        self.A[playerId] = 0