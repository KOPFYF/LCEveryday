class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        int n = arr.length;
        int s = 0, e = n -1;
        
        while (s < n - 1 && arr[s] <= arr[s+1]) s++;
        if (s == n - 1) return 0;
        
        while (e >= s && arr[e-1] <= arr[e]) e--;
        if (e == 0) return n - 1;
        
        int res = Math.min(n - 1 - s, e);
        
        int i = 0, j = e;
        while (i <= s && j < n) {
            if (arr[j] >= arr[i]) {
                System.out.println(res);
                res = Math.min(res, j - i - 1);
                i++;
            }else j++;
        }
        
        return res;
    }
}