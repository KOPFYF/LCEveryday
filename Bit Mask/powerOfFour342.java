class Solution {
    public boolean isPowerOfFour(int n) {
        // (1010101010...101010)2 = (aaaaaaa)16
        // 4^x ^ (1010...1010)2 == 0
        return (n > 0) && ((n & (n - 1)) == 0)
            && ((n & 0xaaaaaaaa) == 0);
        // return (Math.log(n) / Math.log(4)) % 1 == 0;
    }
}