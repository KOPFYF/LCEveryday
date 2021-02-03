# Soln 1
def quickselect1(items, item_index):

    def select(lst, l, r, index):

        # base case
        if r == l:
            return lst

        # choose random pivot
        pivot_index = random.randint(l, r)

        # move pivot to beginning of list
        lst, lst = lst, lst

        # partition
        i = l
        for j in xrange(l+1, r+1):
            if lst < lst:
                i += 1
                lst, lst = lst, lst

        # move pivot to correct location
        lst, lst = lst, lst

        # recursively partition one side only
        if index == i:
            return lst
        elif index < i:
            return select(lst, l, i-1, index)
        else:
            return select(lst, i+1, r, index)

    if items is None or len(items) < 1:
        return None

    if item_index < 0 or item_index > len(items) - 1:
        raise IndexError()

    return select(items, 0, len(items) - 1, item_index)

# Soln 2
# Python3 program of Quick Select
 
# Standard partition process of QuickSort(). 
# It considers the last element as pivot 
# and moves all smaller element to left of 
# it and greater elements to right
def partition(arr, l, r):
     
    x = arr[r]
    i = l
    for j in range(l, r):
         
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
             
    arr[i], arr[r] = arr[r], arr[i]
    return i
 
# finds the kth position (of the sorted array) 
# in a given unsorted array i.e this function 
# can be used to find both kth largest and 
# kth smallest element in the array. 
# ASSUMPTION: all elements in arr[] are distinct
def kthSmallest(arr, l, r, k):
 
    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):
 
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)
 
        # if position is same as k
        if (index - l == k - 1):
            return arr[index]
 
        # If position is more, recur 
        # for left subarray 
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)
 
        # Else recur for right subarray 
        return kthSmallest(arr, index + 1, r, 
                            k - index + l - 1)
    return INT_MAX
 
# Driver Code
arr = [ 10, 4, 5, 8, 6, 11, 26 ]
n = len(arr)
k = 3
print("K-th smallest element is ", end = "")
print(kthSmallest(arr, 0, n - 1, k))
 

# Soln 3
from random import randrange
def partition(x, pivot_index = 0):
    i = 0
    if pivot_index !=0: x[0],x[pivot_index] = x[pivot_index],x[0]
    for j in range(len(x)-1):
        if x[j+1] < x[0]:
            x[j+1],x[i+1] = x[i+1],x[j+1]
            i += 1
    x[0],x[i] = x[i],x[0]
    return x,i

def RSelect(x,k):
    if len(x) == 1:
        return x[0]
    else:
        xpart = partition(x,randrange(len(x)))
        x = xpart[0] # partitioned array
        j = xpart[1] # pivot index
        if j == k:
            return x[j]
        elif j > k:
            return RSelect(x[:j],k)
        else:
            k = k - j - 1
            return RSelect(x[(j+1):], k)
        
x = [3,1,8,4,7,9]
for i in range(len(x)):
    print RSelect(x,i),