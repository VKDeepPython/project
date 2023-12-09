"""LRU Cache with logging options"""


import logging

from singleton import Singleton


logger = logging.getLogger("LRUCache")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("cache.log", 'w')
formatter = logging.Formatter("%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class LRUCache(Singleton):
    """LRU Cache implementation"""
    def __init__(self, limit=42):
        self.limit = limit
        self.cache = {}
        self.head = None
        self.tail = None
        logger.debug("New LRUCache instance created")

    def get(self, key):
        """Get value by key"""
        if key not in self.cache:
            logger.info("Got key='%s' which is not in cache", key)
            return None

        node = self.cache[key]
        self.__move_to_front(node)
        logger.debug("Got key='%s' from cache", key)
        return node.value

    def set(self, key, value):
        """Set key-value"""
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            logger.debug("Updated key='%s'", key)
            self.__move_to_front(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            logger.debug("Added key='%s' to cache", key)
            self.__add_to_front(node)

            if len(self.cache) > self.limit:
                logger.info("Removing last key...")
                self.__remove_last()

    def __add_to_front(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def __remove_last(self):
        if not self.tail:
            return

        last_key = self.tail.key
        last_elem = self.cache.pop(self.tail.key).value
        logger.debug("Removed key='%s', value='%s'", last_key, last_elem)

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def __move_to_front(self, node):
        if node == self.head:
            return

        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

        logger.info("Moved to front key='%s', value='%s'", self.head.key, self.head.value)


class Node:
    """Subclass for LRUCache"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

        logger.debug("New Node instance created")
