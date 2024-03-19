from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        seenP = [[False] * n for _ in range(m)]
        seenA = [[False] * n for _ in range(m)]
        
        def dfs(i: int, j: int, seen: List[List[bool]]) -> None:
            if seen[i][j]:
                return
            seen[i][j] = True
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                    dfs(x, y, seen)
        
        # Traverse from the border cells for both oceans
        for i in range(m):
            dfs(i, 0, seenP)
            dfs(i, n - 1, seenA)
        
        for j in range(n):
            dfs(0, j, seenP)
            dfs(m - 1, j, seenA)
        
        # Find cells reachable from both oceans
        result = [[i, j] for i in range(m) for j in range(n) if seenP[i][j] and seenA[i][j]]
        
        return result
