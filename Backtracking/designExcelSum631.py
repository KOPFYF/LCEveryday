from collections import Counter

class Excel:

    def __init__(self, H: int, W: str):
        # list of dict, value stores numeric, sum stores a Counter() including cell, cnt
        # Counter({(1, 'A'): 2, (1, 'B'): 1, (2, 'A'): 1, (2, 'B'): 1}) (r, c): cnt
        self.cells = [{letter: {"value": 0, "sum": None} for letter in string.ascii_uppercase} for h in range(H + 1)]

    def set(self, r: int, c: str, v: int) -> None:
        self.cells[r][c] = {"value": v, "sum": None}

    def get(self, r: int, c: str) -> int:
        cell = self.cells[r][c]
        addrs = cell.get("sum")
        if not addrs:
            return cell["value"]
        # print(addrs)
        res = 0
        for addr, count in addrs.items():
            res += self.get(*addr) * count
        return res
            
        # return sum(self.get(*addr) * count for addr, count in addrs.items())

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        self.cells[r][c]["sum"] = self._parse(strs)
        return self.get(r, c)
    
    def _parse(self, strs: List[str]):
        counter = Counter()
        for s in strs:
            start, end = s.split(":")[0], s.split(":")[1] if ":" in s else s
            # print(s, start, end) # A1:B2 A1 B2
            for r in range(int(start[1:]), int(end[1:]) + 1): # get row index, 1->2
                for ci in range(ord(start[0]), ord(end[0]) + 1): # get col index, A->B
                    counter[(r, chr(ci))] += 1
        return counter
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)