#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
In this solution as well as in s1, I misunderstood that 
what leetcode gives is the string representation of a 
serialized binary tree, i.e, "{1,2,3,#,#,4,#,#,5}" in 
the my case o(╯□╰)o
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        # @param root, a tree node
        # @return a list of lists of integers
        def levelOrderBottom(self, root):
        	if not root:
        		return []
        		
        	nodes = root.strip('{}').split(',')
        	if not nodes or not nodes[0]:
        		return []
        	
        	result = []

        	current_level_len = 1
        	next_level_len = 0
        	line = []
        	for node in nodes:
        		if node != '#':
        			next_level_len += 2
        			line.append(int(node))
        		current_level_len -= 1
        		if current_level_len == 0:
        			current_level_len = next_level_len
        			next_level_len = 0
        			result.append(line)
        			line = []
        	result.reverse()
        	return result


s = Solution()
print s.levelOrderBottom("{1,2,3,#,#,4,#,#,5}")
print s.levelOrderBottom("{3,9,20,#,#,15,7}")
