# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections


def bfs(r, c, grid, visit):
    numOfRows = len(grid)
    numOfCols = len(grid[0])
    q = collections.deque()
    q.append((r, c))
    visit.add((r, c))

    while q:
        (row, col) = q.popleft()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for (dr,dc) in directions:
            r, c = row + dr, col + dc
            if r in range(numOfRows) and c in range(numOfCols) and grid[r][c] == '1' and (r, c) not in visit:
                q.append((r, c))
                visit.add((r, c))


class Solution:
    # my soln not 100% correct fails
    """def numIslands(self, grid) -> int:
        X = len(grid)
        Y = len(grid[0])
        islands = 0
        islandChar = '2'
        for i in range(0, X):
            for j in range(0, Y):
                if grid[i][j] == '1':
                    grid[i][j] = islandChar
                    temp = islandChar
                    combine = 0
                    entered = False
                    fix = True
                    if not (i == 0 or (grid[i - 1][j] == '0' or grid[i - 1][j] == '1')):
                        grid[i][j] = grid[i - 1][j]
                        if temp == grid[i - 1][j] and temp != grid[i][j - 1]:
                            fix = False
                        combine += 1
                        entered = True
                    if not (j == 0 or (grid[i][j - 1] == '0' or grid[i][j - 1] == '1')):
                        combine += 1
                        if grid[i][j] == grid[i][j - 1] and entered and fix:
                            combine -= 1
                        grid[i][j] = grid[i][j - 1]
                        entered = True
                    if not (i == X - 1 or (grid[i + 1][j] == '0' or grid[i + 1][j] == '1')):
                        combine += 1
                        if grid[i][j] == temp and entered:
                            combine -= 1
                        grid[i][j] = grid[i + 1][j]
                        entered = True
                    if not (j == Y - 1 or (grid[i][j + 1] == '0' or grid[i][j + 1] == '1')):
                        combine += 1
                        if grid[i][j] == temp and entered:
                            combine -= 1
                        grid[i][j] = grid[i][j + 1]
                    if combine == 0:
                        if islands != 0:
                            islandChar = str(int(islandChar) + 1)
                            grid[i][j] = islandChar
                        islands += 1
                    if combine > 1:
                        if grid[i - 1][j - 1] != grid[i - 1][j]:
                            islands -= (combine - 1)
                            print(str(i) + str(j) + str(combine))
        print(grid)
        return islands"""

    def numIslands(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        islands = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == '1' and (i,j) not in visit:
                    bfs(i, j, grid, visit)
                    islands += 1
        return islands


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    gridIn = [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
    print(obj.numIslands(gridIn))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
