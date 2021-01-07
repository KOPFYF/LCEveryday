class Solution:
    def findLatestStep(self, A: List[int], m: int) -> int:
        n = len(A)
        if m == n:
            return m
        ls = [0] * (n + 2)
        res = -1
        for i, a in enumerate(A):
            l, r = ls[a - 1], ls[a + 1]
            if l == m or r == m:
                res = i
            ls[a - l] = l + r + 1
            ls[a + r] = l + r + 1

        return res
    
'''
       arr = [3,5,1,2,4]
       initial len = [0,0,0,0,0,0,0] 
       initial cnt = [0,0,0,0,0,0] 
      
       Step 1:
       a = 3, left = 0 right = 0      //int a = arr[i], left = length[a - 1], right = length[a + 1];
       len = [0,0,0,1,0,0,0]         //length[a] = length[a - left] = length[a + right] = left + right + 1;
       cnt = [-2,1,0,0,0,0]         // count[left]--;   count[right]--; count[length[a]]++;
       res = 1                     // if (count[m]) res = i + 1;
       
       Step 2:
       a = 5, left = 0 right = 0       //int a = arr[i], left = length[a - 1], right = length[a + 1];
       len = [0,0,0,1,0,1,0]          //length[a] = length[a - left] = length[a + right] = left + right + 1;
       cnt = [-4,2,0,0,0,0]          // count[left]--;   count[right]--; count[length[a]]++;
       res = 2                      // if (count[m]) res = i + 1;
       
       Step 3:
       a = 1, left = 0 right = 0           //int a = arr[i], left = length[a - 1], right = length[a + 1];
       len = [0,1,0,1,0,1,0]              //length[a] = length[a - left] = length[a + right] = left + right + 1;
       cnt = [-6,3,0,0,0,0]              // count[left]--;   count[right]--; count[length[a]]++;
       res = 3                          // if (count[m]) res = i + 1;
       
       Step 4:
       a = 2, left = 1 right = 1       //int a = arr[i], left = length[a - 1], right = length[a + 1];
       len = [0,3,3,3,0,1,0]          //length[a] = length[a - left] = length[a + right] = left + right + 1;
       cnt = [-6,1,0,1,0,0]          // count[left]--;   count[right]--; count[length[a]]++;
       res = 4                      // if (count[m]) res = i + 1;
       
       Step 5:
       a = 4, left = 3 right = 1        //int a = arr[i], left = length[a - 1], right = length[a + 1];
       len = [0,5,3,3,5,5,0]           //length[a] = length[a - left] = length[a + right] = left + right + 1;
       cnt = [-6,0,0,0,0,1]           // count[left]--;   count[right]--; count[length[a]]++;
       res = 4                       // if (count[m]) res = i + 1;
   
'''