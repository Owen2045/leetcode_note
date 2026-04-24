from typing import List
from collections import Counter
from typing import Optional



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def gogogo(x, y):
            # 一樣檢查邊界
            if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0 or grid[x][y] == '0':
                return 0
            else:
                # 把走過的填0 這題不用算島嶼面積 所以不用return
                grid[x][y] = '0'
                gogogo(x+1, y)
                gogogo(x-1, y)
                gogogo(x, y+1)
                gogogo(x, y-1)
                
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 是1才走 並且+1就好 因為只算島嶼數量 不算面積
                if grid[i][j] == '1':
                    gogogo(i, j)
                    ans += 1
        return ans


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

a = Solution()
b = a.numIslands(grid)
print(b)

