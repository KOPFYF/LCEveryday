'''
2. you are given an array with 10^8 elements and you must compute the sum A[j] + A[k] for every possible pair of elements
 in the array, How long will this computation take on a single mainstream computer?
a. milliseconds
b. seconds
c. minutes
d. hours
e. more than few hours
'''
import random
import time

def main():
  res = 0
  arr = [1 for _ in range(10**8)]
  for i in range(len(arr)):
    # for j in range(len(arr)):
    res = arr[i] + arr[i]


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))


