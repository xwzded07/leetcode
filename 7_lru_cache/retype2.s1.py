#!/usr/bin/env python
# -*- coding:utf-8 -*-

class CacheNode(object):
    def __init__(self, key=None, value=None, previous=None, next=None):
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.cache = {}

        # use double linked list to track lru node
        self.head = CacheNode()
        self.tail = CacheNode()
        self.head.next = self.tail
        self.tail.previous = self.head

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
        if key in self.cache: # revise existing node
            node = self.cache[key]
            node.value = value
            self.move_head(node)
        elif self.count < self.capacity: # add new node
            node = CacheNode(key, value)
            self.cache[key] = node
            self.put_head(node)
            self.count += 1
        else: # replace existing node
            node = self.tail.previous
            del self.cache[node.key]
            node.key = key
            node.value = value
            self.cache[key] = node
            self.move_head(node)

    def move_head(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
        node.next = self.head.next
        node.previous = self.head
        node.next.previous = node
        node.previous.next = node

    def put_head(self, node):
        node.next = self.head.next
        node.previous = self.head
        node.next.previous = node
        node.previous.next = node



cache = LRUCache(3)
cache.set(1,1)
cache.set(2,2)
cache.set(3,3)
print cache.get(3) # 3
print cache.get(5) # -1
cache.set(1, 4)
cache.set(4, 5)
print cache.get(1) # 4
print cache.get(2) # -1
print cache.get(4) # 5