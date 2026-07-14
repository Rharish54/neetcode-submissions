class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        visited = set()
        total_islands = 0

        def bfs(r, c):
            # iterative DS -- not recursive
            my_queue = collections.deque()
            visited.add((r, c))
            my_queue.append((r, c))

            while my_queue: #basically saying while que not empty
                rows, cols = my_queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = rows + dr, cols + dc
                    #check to see if in bounds
                    if r in range(row) and c in range(col) and grid[r][c] == "1" and (r, c) not in visited:
                        my_queue.append((r, c))
                        visited.add((r, c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    total_islands += 1
        
        return total_islands