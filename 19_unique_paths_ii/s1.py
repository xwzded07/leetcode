#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])

        paths = [[0 for col in xrange(0, width)] for row in xrange(0, height)]

        paths[0][0] = 1
        for col in xrange(1, width):
            paths[0][col] = 1 if paths[0][col-1] == 1 and obstacleGrid[0][col] == 0 else 0
        for row in xrange(1, height):
            paths[row][0] = 1 if paths[row-1][0] == 1 and obstacleGrid[row][0] == 0 else 0

        for row in xrange(1, height):
            for col in xrange(1, width):
                if obstacleGrid[row][col] == 1:
                    paths[row][col] = 0
                else:
                    paths[row][col] += paths[row][col-1]
                    paths[row][col] += paths[row-1][col]

        return paths[height-1][width-1]

plane = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
s = Solution()
print s.uniquePathsWithObstacles(plane) # 2