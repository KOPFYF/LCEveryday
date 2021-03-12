public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int cnt = 0, mask = 1;
        for (int i = 0; i < 32; i++) {
            if ((n & mask) != 0)
                cnt++;
            mask <<= 1;
        }
        return cnt;
    }
    
    public int hammingWeight(int n) {
        int cnt = 0;
        while (n != 0) {
            cnt++;
            n &= (n - 1); // set the right most 1 to 0
        }
        return cnt;
    }
    
    public int hammingWeight(int n) {
        return Integer.bitCount(n);
    }
    
}