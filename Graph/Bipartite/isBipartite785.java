class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] colors = new int[n];
        for (int i = 0; i < n; i++) {
            if (colors[i] == 0 && !dfs(graph, colors, 1, i)) 
                return false;
        }
        return true;
    }
    
    private boolean dfs(int[][] graph, int[] colors, int color, int cur) {
        // can we paint current node with color?
        if (colors[cur] != 0)
            return colors[cur] == color;
        colors[cur] = color;
        for (int nxt: graph[cur]) {
            if (!dfs(graph, colors, -color, nxt))
                // try print all neighbors with oppo-color
                return false;
        }
        return true;
    }
}