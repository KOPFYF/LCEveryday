class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        hs, ms = (int(x) for x in startTime.split(":"))
        ts = 60 * hs + ms
        hf, mf = (int(x) for x in finishTime.split(":"))
        tf = 60 * hf + mf
        return tf // 15 - (ts + 14) // 15 + (ts > tf) * 96