#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        
        p = head
        next = p.next
        while next:
            if p.val == next.val:
                next = next.next
            else:
                p.next = next
                p = next
                next = p.next
        p.next = next
        
        return head

def tranverseList(head):
	node = head
	while node:
		print node.val
		node = node.next

s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(2)
n6 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

tranverseList(s.deleteDuplicates(n1))


