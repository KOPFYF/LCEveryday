from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock_zero = Lock()
        self.lock_even = Lock()
        self.lock_odd = Lock()
        
        # init: release 0 and lock the other 2
        self.lock_even.acquire()
        self.lock_odd.acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.lock_zero.acquire()
            printNumber(0)
            if i & 1:
                self.lock_odd.release()
            else:
                self.lock_even.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.lock_even.acquire()
            printNumber(i)
            self.lock_zero.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.lock_odd.acquire()
            printNumber(i)
            self.lock_zero.release()
        
        