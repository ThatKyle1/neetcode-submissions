class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # some how use dfs to count 1's near each other and keep track of count using max()
        # 
        
        def dfs(index):
            
            queue = deque()
            queue.append(index)
            visited.add(index)
            count = 0
            while queue:
                cRow, cCol = queue.popleft()
                count += 1
                for i in directions:
                    dRow, dCol = i # direction that it check
                    nRow = cRow + dRow
                    nCol = cCol + dCol

                    if nRow >= 0 and nRow < maxRow and nCol >=0 and nCol < maxCol:
                        if (nRow, nCol) in visited:
                            continue
                        if grid[nRow][nCol] == 1:
                            queue.append((nRow, nCol))
                            visited.add((nRow, nCol))

            return count




        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        maxRow = len(grid)
        maxCol = len(grid[0])
        maxCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxCount = max(dfs((row, col)), maxCount)

        return maxCount

