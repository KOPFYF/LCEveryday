class StringIterator:

    def __init__(self, compressedString: str):
        self.word = compressedString + '#'
        self.decode = ""
        tmp = ""
        num = ""
        for i, ch in enumerate(self.word):
            if not ch.isdigit():
                self.decode += ch
                tmp = ch
            else:
                num += ch
                if int(num) > 100:
                    self.decode += (int(num) - 1) * tmp
                    num = ""
                    break
                elif not self.word[i + 1].isdigit():
                    self.decode += (int(num) - 1) * tmp
                    num = ""
            if i > 100:
                break

        self.decode = deque(list(self.decode[:-1]))

    def next(self) -> str:
        if self.hasNext():
            return self.decode.popleft()
        else:
            return " "

    def hasNext(self) -> bool:
        return len(self.decode) > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()