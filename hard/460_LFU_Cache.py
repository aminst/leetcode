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

    def deleteNode(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.next = None
        del self.key_to_node[node.key]

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
        return key

    def hasKey(self, key):
        return key in self.key_to_node

    def updateValue(self, key, value):
        self.key_to_node[key].value = value

    def getValue(self, key):
        return self.key_to_node[key].value
    
    def getSize(self):
        return len(self.key_to_node)

class SeqLinks:
    def __init__(self, capacity):
        self.freq_to_nodes = dict()
        self.key_to_freq_node = dict() # map of key to tuple of (freq, node)
        self.lowest_freq = None
        self.capacity = capacity

    def printSeqLinks(self):
        for freq, nodes in self.freq_to_nodes.items():
            print("FREQ ", freq)
            nodes.printList()
        print("LOWEST_FREQ ", self.lowest_freq)
        print("Key To Freq Node", self.key_to_freq_node)

    def removeNodeFromLowestFreq(self):
        key = self.freq_to_nodes[self.lowest_freq].deleteLeastUsed()
        del self.key_to_freq_node[key]
        if self.freq_to_nodes[self.lowest_freq].getSize() == 0:
            del self.freq_to_nodes[self.lowest_freq]
            self.lowest_freq = 1

    def removeNodeFromFreq(self, freq, node):
        self.freq_to_nodes[freq].deleteNode(node)
        del self.key_to_freq_node[node.key]

    def addNodeToFreq(self, freq, node):
        if freq not in self.freq_to_nodes:
            self.freq_to_nodes[freq] = LRULinkedList()
        if self.lowest_freq == None:
            self.lowest_freq = freq
        if freq < self.lowest_freq:
            self.lowest_freq = freq
        self.freq_to_nodes[freq].addNode(node)
        self.key_to_freq_node[node.key] = (freq, node)

    def increaseFreq(self, key):
        freq, node = self.key_to_freq_node[key]
        self.removeNodeFromFreq(freq, node)
        if self.freq_to_nodes[freq].getSize() == 0:
            if self.lowest_freq == freq:
                self.lowest_freq += 1
            del self.freq_to_nodes[freq]
        self.addNodeToFreq(freq+1, node)

    def hasKey(self, key):
        return key in self.key_to_freq_node
    
    def updateKey(self, key, value):
        freq, node = self.key_to_freq_node[key]
        node.value = value

    def getKey(self, key):
        freq, node = self.key_to_freq_node[key]
        return node.value
    
    def willExceedCapacity(self):
        return len(self.key_to_freq_node) + 1 > self.capacity       


class LFUCache:
    def __init__(self, capacity: int):
        self.seq_links = SeqLinks(capacity)

    def get(self, key: int) -> int:
        if not self.seq_links.hasKey(key):
            return -1
        self.seq_links.increaseFreq(key)
        return self.seq_links.getKey(key)


    def put(self, key: int, value: int) -> None:
        if self.seq_links.hasKey(key):
            self.seq_links.increaseFreq(key)
            self.seq_links.updateKey(key, value)
        else:
            if self.seq_links.willExceedCapacity():
                self.seq_links.removeNodeFromLowestFreq()
            self.seq_links.addNodeToFreq(1, LRUNode(None, None, key, value))


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
