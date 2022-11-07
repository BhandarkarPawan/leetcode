class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.lru = Node()
        self.mru = Node()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        return_value = self.map[key].value

        accessed_node = self.map[key]
        accessed_node.prev.next = accessed_node.next
        accessed_node.next.prev = accessed_node.prev

        self.mru.next = accessed_node
        accessed_node.prev = self.mru
        self.mru = accessed_node

        return return_value

    def put(self, key: int, value: int):
        new_node = Node(key, value)

        if key in self.map:
            old_node = self.map[key]
            old_node.prev.next = old_node.next
            old_node.next.prev = old_node.prev
            self.map[key] = new_node

        elif len(self.map) == self.capacity:
            removed_node = self.lru
            del self.map[removed_node.key]

            self.lru = self.lru.next
            self.lru.prev = None

        self.mru.next = new_node
        new_node.prev = self.mru
        self.mru = new_node
