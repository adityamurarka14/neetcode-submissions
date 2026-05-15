class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0,1], [-1, 0], [0, -1]]
        gatesQueue = deque()
        maxDist = 5
        visited = set()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    gatesQueue.append((x,y))
                    visited.add((x,y))
        print(gatesQueue, 'main')
        for r,c in gatesQueue:
            grid[r][c] = 5
        while gatesQueue:
            currR, currC = gatesQueue.popleft()
            for a,b in directions:
                r, c = a + currR, b + currC
                if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] and grid[r][c] != 0 and (r,c) not in visited:
                    grid[r][c] = grid[currR][currC] + 1
                    maxDist = max(maxDist, grid[currR][currC] + 1)
                    gatesQueue.append((r, c))
                    visited.add((r, c))
                    print(r, c, grid[currR][currC] + 1)
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    return -1

        return maxDist - 5