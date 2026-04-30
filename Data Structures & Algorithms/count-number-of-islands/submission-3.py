class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(1,0), (0,1), (-1, 0), (0, -1)]

        maxRow = len(grid)
        maxCol = len(grid[0])

        numIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1" and (row, col) not in visited:
                    queue = deque()
                    visited.add((row, col))
                    queue.append((row, col))
                    while queue:
                        cRow, cCol = queue.popleft()
                        for dRow, dCol in directions:
                            nRow = cRow + dRow
                            nCol = cCol + dCol
                            if nRow >= 0 and nRow < maxRow and nCol >= 0 and nCol < maxCol:
                                if grid[nRow][nCol] == "1" and (nRow, nCol) not in visited:
                                    visited.add((nRow, nCol))
                                    queue.append((nRow, nCol))
                    numIslands += 1

        return numIslands