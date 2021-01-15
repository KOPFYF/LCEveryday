class Solution {
    public boolean canReach(int[] arr, int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        Set<Integer> seen = new HashSet<>(start);
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            if (arr[cur] == 0) return true;
            
            for (int nxt : new int[]{cur - arr[cur], cur + arr[cur]}) {
                if (0 <= nxt && nxt < arr.length && !seen.contains(nxt)) {
                    q.offer(nxt);
                    seen.add(nxt);
                }
            }
        }
        return false;
    }
}