# https://leetcode.com/problems/fizz-buzz-multithreaded/discuss/542960/python-greater99.28-a-standard-Lock()-based-solution-with-detailed-explanation
from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        '''
        Lock(). It's basically a flag and it can be either acquired or released. 
        So an acquire() call will wait until Lock is released. 
        Originally locks are created as released
        First of all, when the class is initialized, we want only the main thread to be released, the other three threads should stay locked. 
        '''
        self.n = n
        self.f, self.b, self.fb, self.main = Lock(), Lock(), Lock(), Lock()
        self.f.acquire() # init: lock it
        self.b.acquire()
        self.fb.acquire()
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
    	while True:
            self.f.acquire() # lock it
            if self.n == 0: # global flag to stop
                return
            printFizz() # call function
            self.main.release() # release the main lock

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while True:
            self.b.acquire()
            if self.n == 0:
                return
            printBuzz()
            self.main.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.n == 0:
                return
            printFizzBuzz()
            self.main.release()


    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        '''
        the number thread is going to acquier its own lock, then it will check the current number, 
        if it's %15, %3 or %5 - it's going to release a corresponding lock, 
        otherwise it's going to print the number itself and release its own lock.
        '''
        for i in range(1, self.n + 1):
            #print("number:",i)
            self.main.acquire()
            if i % 15 == 0:
                self.fb.release()
            elif i % 3 == 0:
                self.f.release()
            elif i % 5 == 0:
                self.b.release()
            else:
                printNumber(i)
                self.main.release() # main lock works only num % 15 != 0

        self.main.acquire() 
        self.n = 0 # Use some global variable to tell all threads to stop or continue.
        self.f.release()
        self.b.release()
        self.fb.release()
        return



class FizzBuzz2:
    def __init__(self, n):
        self.n = n
        self.f = threading.Lock()
        self.b = threading.Lock()
        self.fb = threading.Lock()
        self.main = threading.Lock()        
        self.f.acquire()
        self.b.acquire()
        self.fb.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        for i in range (self.n // 3 - self.n // 15):
            self.f.acquire()
            printFizz()
            self.main.release()
            
    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        for i in range (self.n // 5 - self.n // 15):
            self.b.acquire()
            printBuzz()
            self.main.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        for i in range (self.n // 15):
            self.fb.acquire()
            printFizzBuzz()
            self.main.release()        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        for i in range(1, self.n + 1):         
            self.main.acquire()        
            if i % 15 == 0:
                self.fb.release()
            elif i % 3 == 0:
                self.f.release()
            elif i % 5 == 0:
                self.b.release()
            else:
                printNumber(i)
                self.main.release()             