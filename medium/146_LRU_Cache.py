class LRUNode:
    def __init__(self, prev, next, key, value):
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value
    
    def __str__(self):
        prev_key = None
        next_key = None
        if self.prev:
            prev_key = self.prev.key
        if self.next:
            next_key = self.next.key
        return "Prev: {} Next {} Key {} Value {}".format(prev_key, next_key, self.key, self.value)

class LRULinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.key_to_node = dict()
    
    def printList(self):
        print("List Head: ", self.head)
        print("List Tail: ", self.tail)
        print("Key To Node: ", self.key_to_node)
        temp = self.head
        while(temp):
            print(temp)
            temp = temp.next
        print("********")
    
    def addNode(self, node):
        if self.head == None:
            self.head = node
        if self.tail != None:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.key_to_node[node.key] = node

    def moveNodeToEnd(self, key):
        node = self.key_to_node[key]
        if node == self.tail:
            return
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = self.tail
        self.tail.next = node
        node.next = None
        self.tail = node

    def deleteLeastUsed(self):
        key = self.head.key
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        del self.key_to_node[key]

    def hasKey(self, key):
        return key in self.key_to_node

    def updateValue(self, key, value):
        self.key_to_node[key].value = value

    def getValue(self, key):
        return self.key_to_node[key].value
    
    def getSize(self):
        return len(self.key_to_node)

class LRUCache:
    def __init__(self, capacity: int):
        self.nodes = LRULinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if self.nodes.hasKey(key) == False:
            return -1
        self.nodes.moveNodeToEnd(key)
        return self.nodes.getValue(key)

    def put(self, key: int, value: int) -> None:
        if self.nodes.hasKey(key):
            self.nodes.moveNodeToEnd(key)
            self.nodes.updateValue(key, value)
        else:
            self.nodes.addNode(LRUNode(None, None, key, value))
        if self.nodes.getSize() > self.capacity:
            self.nodes.deleteLeastUsed()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
