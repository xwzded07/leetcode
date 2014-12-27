#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        s = []  # use list to simulate stack
        idx = 0
        max_area = 0
        
        while idx < len(height):
            if len(s) == 0 or height[s[-1]] <= height[idx]:
                s.append(idx)
                idx += 1
            else:
                bar = s.pop()
                start = -1 if len(s) == 0 else s[-1]
                max_area = max(max_area, (idx - start -1) * height[bar])

        while len(s) != 0:
                bar = s.pop()
                start = -1 if len(s) == 0 else s[-1]
                max_area = max(max_area, (idx - start -1) * height[bar])
            
        return max_area

s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3]) # 10
print s.largestRectangleArea([0,1,0,1]) # 1
