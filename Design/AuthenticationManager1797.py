class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.map = {} # key is id, value is expired time
        self.gap = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.map[tokenId] = (currentTime, currentTime + self.gap)

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.map:
            s, e = self.map[tokenId]
            if currentTime < e:
                self.map[tokenId] = (s, currentTime + self.gap)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for k, v in self.map.items():
            if currentTime < v[1]:
                cnt += 1
        return cnt