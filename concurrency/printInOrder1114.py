from threading import Lock

class Foo:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()
        
    def first(self, printFirst):
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.locks[0].release()
        
    def second(self, printSecond):
        # Wait for the first job to be done
        with self.locks[0]:
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.locks[1].release()
            
            
    def third(self, printThird):
        # Wait for the second job to be done.
        with self.locks[1]:
            printThird()