class Solution {
    public boolean isPowerOfTwo(int n) {
    	// O(1)
        // turn off the right most 1
        // power of 2 would only has one bit of 1.
        return n > 0 && (n & (n - 1)) == 0;
    }
}