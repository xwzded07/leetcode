#!/usr/bin/env python

"""
Got trapped at a little syntax error, 
lint is as important as carefullness.
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
            
        result = []
        
        nodes = [root] # list of all nodes
        idx = 0
        current_line_start = 0
        current_line_end = 0
        while idx < len(nodes):
            node = nodes[idx]
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            if idx == current_line_end:
                result.append([x.val for x in nodes[current_line_start:current_line_end+1]])
                current_line_start = current_line_end + 1
                current_line_end = len(nodes) - 1
            idx += 1
            
        return result


root = TreeNode(1)
n3 = TreeNode(3)
n5 = TreeNode(5)
n7 = TreeNode(7)
root.left = n3
root.right = n5
n3.right = n7

s = Solution()
print s.levelOrder(root)