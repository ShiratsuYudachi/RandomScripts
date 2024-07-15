from math import *
from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[inf]*cols for _ in range(rows)]

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if r==rows-1 and c==cols-1:
                    dp[r][c] = max(-dungeon[r][c]+1,1)
                elif r==rows-1:
                    dp[r][c] = max(dp[r][c+1]-dungeon[r][c],1)
                elif c==cols-1:
                    dp[r][c] = max(dp[r+1][c]-dungeon[r][c],1)
                else:
                    dp[r][c] = max(min(dp[r+1][c],dp[r][c+1])-dungeon[r][c],1)
        return dp[0][0]

solution = Solution()
print(solution.calculateMinimumHP([[0,-3]]))