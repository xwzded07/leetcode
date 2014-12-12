#!/usr/bin/env python
# -*- coding:utf-8 -*-
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
            
        result = [] # final result, list of levels
        current_line = []
        next_line = [root]
        while next_line:
            current_line = next_line
            next_line = []
            result.append([x.val for x in current_line])
            for node in current_line:
                if node.left:
                    next_line.append(node.left)
                if node.right:
                    next_line.append(node.right)
        result.reverse()
        
        return result