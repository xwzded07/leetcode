#!/usr/bin/env python
# -*- coding:utf-8 -*-

class CacheNode:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.count = 0

        # double linked list
        self.head = CacheNode()
        self.tail = CacheNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        # use a list as node pool
        self.available_nodes = []
        for i in xrange(0, capacity):
            self.available_nodes.append(CacheNode())

    # @return an integer
    def get(self, key):
        """
         Get the value (will always be positive) of the key 
         if the key exists in the cache, otherwise return -1.
        """
        if key in self.cache:
            node = self.cache[key]
            self.move_head(node)
            return node.value
        else:
            return -1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        """
        Set or insert the value if the key is not already present. 
        When the cache reached its capacity, it should invalidate 
        the least recently used item before inserting a new item.
        """
        if key in self.cache: # revise existing record
            node = self.cache[key]
            node.value = value
            self.move_head(node)
        elif self.count != self.capacity: # add new record
            self.count += 1
            node = self.available_nodes.pop()
            node.key = key
            node.value = value
            self.insert_head(node)
            self.cache[key] = node

        else: # cache full, revise existing record
            node = self.tail.prev
            del self.cache[node.key]
            node.key = key
            node.value = value
            self.move_head(node)
            self.cache[key] = node

    def insert_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.prev.next = node
        node.next.prev = node
            

    def move_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        node.prev.next = node


cache = LRUCache(3)
cache.set(1,1)
cache.set(2,2)
cache.set(3,3)
print cache.get(3) # 3
print cache.get(5) # -1
cache.set(3, 4)
cache.set(4, 5)
print cache.get(1) # -1
print cache.get(3) # 4
print cache.get(4) # 5




