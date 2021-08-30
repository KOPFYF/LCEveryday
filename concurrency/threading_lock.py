# https://docs.python.org/3/library/threading.html

'''

class threading.Lock
The class implementing primitive lock objects. Once a thread has acquired a lock, subsequent attempts to acquire it block, until it is released; any thread may release it.

Note that Lock is actually a factory function which returns an instance of the most efficient version of the concrete Lock class that is supported by the platform.

acquire(blocking=True, timeout=-1)
Acquire a lock, blocking or non-blocking.

When invoked with the blocking argument set to True (the default), block until the lock is unlocked, then set it to locked and return True.

When invoked with the blocking argument set to False, do not block. If a call with blocking set to True would block, return False immediately; otherwise, set the lock to locked and return True.

When invoked with the floating-point timeout argument set to a positive value, block for at most the number of seconds specified by timeout and as long as the lock cannot be acquired. A timeout argument of -1 specifies an unbounded wait. It is forbidden to specify a timeout when blocking is false.

The return value is True if the lock is acquired successfully, False if not (for example if the timeout expired).

Changed in version 3.2: The timeout parameter is new.

Changed in version 3.2: Lock acquisition can now be interrupted by signals on POSIX if the underlying threading implementation supports it.

release()
Release a lock. This can be called from any thread, not only the thread which has acquired the lock.

When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.

When invoked on an unlocked lock, a RuntimeError is raised.

There is no return value.

locked()
Return true if the lock is acquired.

'''


# https://stackoverflow.com/questions/10525185/python-threading-how-do-i-lock-a-thread

import threading
import time
import inspect

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

count = 0
lock = threading.Lock()

def incre():
    global count
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print "Inside %s()" % caller
    print "Acquiring lock"
    with lock:
        print "Lock Acquired"
        count += 1  
        time.sleep(2)  

def bye():
    while count < 5:
        incre()

def hello_there():
    while count < 5:
        incre()

def main():    
    hello = Thread(hello_there)
    goodbye = Thread(bye)



# https://www.educative.io/edpresso/what-are-locks-in-python

# Importing the threading module
import threading 
# Declraing a lock
lock = threading.Lock()
deposit = 100

# Function to add profit to the deposit
def add_profit(): 
    global deposit
    for i in range(100000):
        lock.acquire()
        deposit = deposit + 10
        lock.release()

# Function to deduct money from the deposit
def pay_bill(): 
    global deposit
    for i in range(100000):
        lock.acquire()
        deposit = deposit - 10
        lock.release()

# Creating threads
thread1 = threading.Thread(target = add_profit, args = ())
thread2 = threading.Thread(target = pay_bill, args = ())
# Starting the threads  
thread1.start() 
thread2.start() 
# Waiting for both the threads to finish executing 
thread1.join()
thread2.join()
# Displaying the final value of the deposit
print(deposit)
