# Author: Huahua
class MinHeap:
  def __init__(self, data = None):
    self.data = list(data) if data else []
    for i in range((len(self.data)) // 2, -1, -1):
      self.heapifyDown(i)
 
  def push(self, key):
    self.data.append(key)
    self.heapifyUp(len(self.data) - 1)
 
  def pop(self):
    self.swap(0, -1)
    min_el = self.data.pop()
    self.heapifyDown(0)
    return min_el
 
  def size(self):
    return len(self.data)
 
  def swap(self, i, j):
    self.data[i], self.data[j] = self.data[j], self.data[i]
 
  def heapifyDown(self, i):
    smallest = i
    for c in [2 * i + 1, 2 * i + 2]:
      if c < self.size() and self.data[c] < self.data[smallest]: smallest = c
    if smallest != i:
      self.swap(i, smallest)
      self.heapifyDown(smallest)
 
  def heapifyUp(self, i):
    if i == 0: return
    parent = (i - 1) // 2
    if self.data[i] >= self.data[parent]: return
    self.swap(i, parent)
    self.heapifyUp(parent)
 
def test():
  data = [5,1,3,5,3,4,3,7]
  heap = MinHeap()
  for x in data: heap.push(x)
  output = []
  while heap.size():
    output.append(heap.pop())
  assert output == sorted(data)
 
def testBuildHeap():
  data = [5,1,3,5,3,4,3,7]
  heap = MinHeap(data)
  output = []
  while heap.size():
    output.append(heap.pop())
  assert output == sorted(data)
 
def main():
  test()
  testBuildHeap()
 
if __name__ == '__main__':
  main()