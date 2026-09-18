class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0            
        rows = len(grid)
        columns = len(grid[0])
        count = 0        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    count += 1
                    q = deque()
                    q.append((r, c))
                    grid[r][c] = '0'  # Mark the starting cell as visited immediately                    
                    while q:
                        row, col = q.popleft()
                        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]                        
                        for dr, dc in directions:
                            next_row = row + dr
                            next_col = col + dc                            
                            # Fixed the boundary condition here (0 <= next_row)
                            if (0 <= next_row < rows) and (0 <= next_col < columns) and grid[next_row][next_col] == '1':
                                q.append((next_row, next_col))
                                grid[next_row][next_col] = '0'  # Mark as visited right when adding to queue                                
        return count