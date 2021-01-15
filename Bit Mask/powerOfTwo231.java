class Solution {
    public boolean isPowerOfTwo(int n) {
        // turn off the right most 1
        return n > 0 && (n & (n - 1)) == 0;
    }
}