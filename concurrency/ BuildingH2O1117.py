from threading import Lock

class H2O:
    def __init__(self):
        self.lock_h, self.lock_o = Lock(), Lock()
        self.lock_o.acquire() # H comes first, so lock O
        self.cnt = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.lock_h.acquire()
        self.cnt += 1
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        if self.cnt == 2:
            self.cnt = 0 # reset
            self.lock_o.release() # release O only after we see 2 Hs
        else:
            self.lock_h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.lock_o.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.lock_h.release()


# soln 2, barrier
'''
Barrier Objects
New in version 3.2.

This class provides a simple synchronization primitive for use by a fixed number of threads that need to wait for each other. 
Each of the threads tries to pass the barrier by calling the wait() method 
and will block until all of the threads have made their wait() calls. At this point, the threads are released simultaneously.

The barrier can be reused any number of times for the same number of threads.


Hint:

You have a waiting area.
No more than two hydrogens are allowed into the waiting area at a time.
No more than one oxygen is allowed into the waiting area at a time.
Once the waiting area is full (and before admitting any additional atoms), 
the three waiting atoms leave together to form a molecule.
'''
from threading import Barrier, Semaphore
class H2O:
    def __init__(self):
        self.b = Barrier(3)
        self.h = Semaphore(2)
        self.o = Semaphore(1)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        self.b.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        self.b.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o.release()


class H2O:
    def __init__(self):
        self.b = Barrier(3)
        self.h = Semaphore(2)
        self.o = Semaphore(1)

    def hydrogen(self, releaseHydrogen):
        with self.h:
            self.b.wait()
            releaseHydrogen()

    def oxygen(self, releaseOxygen):
        with self.o:
            self.b.wait()
            releaseOxygen()