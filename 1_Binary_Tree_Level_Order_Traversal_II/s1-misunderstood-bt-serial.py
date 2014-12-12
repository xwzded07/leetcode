#/usr/bin/env python
# -*- coding:utf-8 -*-

"""
In this solution I misundersood binary tree serialization of leetcode, thinking of the tree as a binary heap, and all empty nodes are replaced by '#'
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
    	root = root.strip('{}')
    	nodes = root.split(',')
    	h = 0
    	n = 1
    	while True:
    		if n  > len(nodes):
    			break
    		n = n * 2
    		h += 1
    	print n,h
    	result = []
    	for x in xrange(0, h):
    		start = n/2 - 1
    		end = min(len(nodes), n-1)
    		line = [x for x in nodes[start:end] if x != '#' ]
    		result.append(line)
    		n /= 2
    		h -= 1

    	return result


s = Solution()
print s.levelOrderBottom("{1,2,3,#,#,4,#,#,#,#,#,5}")
print s.levelOrderBottom("{}")
