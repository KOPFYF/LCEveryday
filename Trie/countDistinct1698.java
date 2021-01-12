class Node {
    Node[] children = new Node[26];
}

class Solution {
    public int countDistinct(String s) {
        Node root = new Node();
        int res = 0, n = s.length();
        for (int i = 0; i < n; i++) {
            Node cur = root;
            for (int j = i; j < n; j++) {
                if (cur.children[s.charAt(j) - 'a'] == null) {
                    cur.children[s.charAt(j)- 'a'] = new Node();
                    res++;
                }
                cur = cur.children[s.charAt(j)- 'a'];
            }
        }
        return res;
    }
}