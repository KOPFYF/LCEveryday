class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;
        
        char[] ch = s.toCharArray(); 
        int res = 0;
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int j = 0, i = 0; j < s.length(); j++) {
            if (map.containsKey(ch[j])) {
                // i cannot go backward, "abba"
                i = Math.max(map.get(ch[j]) + 1, i); 
            } 
            map.put(ch[j], j);   
            res = Math.max(res, j - i + 1);    
        }
        return res;
    }
}