class Solution {
    public int countVowelStrings(int n) {
    //                a  e  i  o  u
    //     initialy: {1, 1, 1, 1, 1}   
    //      n == 1 : {5, 4, 3, 2, 1}   
    //      n == 2 : {15,10,6, 3, 1}   
    //      n == 3 : {35,20,10,4, 1}   
       
        int[] permutation = {1,1,1,1,1};
        
        for(int i = 0; i < n; i++){
            for(int j = permutation.length-1; j>=1; j--){
                permutation[j - 1] += permutation[j];
            }
        }
        
        return permutation[0];
    }
}