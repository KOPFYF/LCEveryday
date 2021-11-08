class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        new_img = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tmp, cnt = 0, 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            tmp += img[ni][nj]
                            cnt += 1
                new_img[i][j] = tmp // cnt
        return new_img