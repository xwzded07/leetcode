#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        last_height = 0
        stack = []

        capacity = 0
        idx = 0
        while  True:
            if idx >= len(A):
                break
            print '+++',A[idx],idx
            print '===',stack
            print '---',capacity
            if A[idx] == 0:
                last_height = 0
                idx += 1
            elif not stack:
                stack.append((A[idx], idx))
                last_height = 0
                idx += 1
            elif stack[-1][0] > A[idx]:
                capacity += (idx - stack[-1][1] - 1) * (A[idx] - last_height)
                stack.append((A[idx], idx))
                last_height = 0
                idx += 1
            else:
                capacity += (idx - stack[-1][1] - 1) * (stack[-1][0] - last_height)
                last_height = stack[-1][0]
                del stack[-1]

        return capacity

s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) # 6
print s.trap([2,4,5,6,8,5,5,0,0,0,3,3]) # 9