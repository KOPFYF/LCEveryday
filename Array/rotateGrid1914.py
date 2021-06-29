class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layer = 1
        total_layer = min(m//2, n//2)
        res = [[0] * n for _ in range(m)]
        while layer <= total_layer:
            nums = []
            # i = layer - 1
            for j in range(layer-1, n-layer+1):
                nums.append(grid[layer-1][j])
            # j = n - layer
            for i in range(layer, m-layer+1):
                nums.append(grid[i][n-layer])
            # i = m - layer 
            for j in range(n-layer-1, layer-2, -1):
                nums.append(grid[m-layer][j])
            # j = layer - 1
            for i in range(m-layer-1, layer-1, -1):
                nums.append(grid[i][layer-1])
                
            # print(layer, nums)
            steps = k % (len(nums))
            nums = nums[steps:] + nums[:steps]
            
            idx = 0
            # i = layer - 1
            for j in range(layer-1, n-layer+1):
                res[layer-1][j] = nums[idx]
                idx += 1
            # j = n - layer
            for i in range(layer, m-layer+1):
                res[i][n-layer] = nums[idx]
                idx += 1
            # i = m - layer 
            for j in range(n-layer-1, layer-2, -1):
                res[m-layer][j] = nums[idx]
                idx += 1
            # j = layer - 1
            for i in range(m-layer-1, layer-1, -1):
                res[i][layer-1] = nums[idx]
                idx += 1
            
            layer += 1
        
        return res