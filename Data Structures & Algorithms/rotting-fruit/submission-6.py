class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0,1], [-1, 0], [0, -1]]
        rottenQueue = deque()
        maxDist = 5
        count = 0
        # visited = set()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    rottenQueue.append((x,y))
                    # visited.add((x,y))
        # print(rottenQueue, 'main')
        # for r,c in rottenQueue:
        #     grid[r][c] = 5
        # while rottenQueue:
        #     currR, currC = rottenQueue.popleft()
        #     for a,b in directions:
        #         r, c = a + currR, b + currC
        #         if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] and grid[r][c] != 0 and (r,c) not in visited:
        #             grid[r][c] = grid[currR][currC] + 1
        #             maxDist = max(maxDist, grid[currR][currC] + 1)
        #             rottenQueue.append((r, c))
        #             visited.add((r, c))
        #             print(r, c, grid[currR][currC] + 1)
        
        # for x in range(rows):
        #     for y in range(cols):
        #         if grid[x][y] == 1:
        #             return -1

        # return maxDist - 5
        fresh = any(1 in row for row in grid)

        # if no rotten source exists
        if not rottenQueue:
            return -1 if fresh else 0
        while rottenQueue:
            for i in range(len(rottenQueue)):
                currR, currC = rottenQueue.popleft()
                for a,b in directions:
                    r, c = a + currR, b + currC
                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] and grid[r][c] == 1:
                        grid[r][c] = 2
                        rottenQueue.append((r, c))
            count += 1

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    return -1

        return count - 1