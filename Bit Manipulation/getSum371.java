class Solution {
    // 011 3
    //+101 5
    //1000 8
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = a & b; // 101 & 011 = 001
            a = a ^ b; // a = 101 ^ 011 = 110
            b = carry << 1; // b = 00 << 1 = 0
        }
        return a; // a = 11 = 3
    }
    
    // recursive
    public int getSum(int a, int b) {
        return b == 0 ? a : getSum(a ^ b, (a & b) << 1);
    }
}