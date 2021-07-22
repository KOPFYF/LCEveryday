def find_array_quadruplet(arr, s):
  '''
  [2, 7, 4, 0, 9, 5, 1, 3]
  s = 20
  
  s = 18 with 3 numbers
  s = 14 with 2 numbers left
  s = 5 with 1 number left
  (2, 4, 9, 5)
  
  [1,1,1,-1,1]
  s = 2
  
  n = len(arr)
  time: O(n)
  space: O(n)
  '''
  res = [float('inf'), float('inf'), float('inf'), float('inf')]
  def dfs(target, cnt, pos, path):
    # it means with cnt number left, index=pos, 
    if pos == len(arr): # to the end of the arr
      return 
    if cnt == 1 and target == arr[pos]:
      res = path + [arr[pos]]
      return

    
    # take the current pos
    dfs(target - arr[pos], cnt - 1, pos + 1, path + [arr[pos]])
    # dont take current pos
    dfs(target, cnt, pos + 1, path)  
    
 
  # If such a quadruplet doesn’t exist, return an empty array.    
  dfs(s, 4, 0, [])
  if res == [float('inf'), float('inf'), float('inf'), float('inf')]:
    return []
  else:
    return sorted(res)
  
  
s = 20

arr = [2, 7, 4, 0, 9, 5, 1, 3]

print(find_array_quadruplet(arr, s))