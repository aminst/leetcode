class TrieNode:
    def __init__(self, is_final):
        self.child_map = dict() # map of char to TrieNode
        self.is_final = is_final

    def add_child(self, char, child_node):
        if char in self.child_map:
            if child_node.is_final:
                self.child_map[char].is_final = True
            return
        self.child_map[char] = child_node

    def get_child(self, char):
        if char not in self.child_map:
            return None
        return self.child_map[char]

class Trie:
    def __init__(self):
        self.root_node = TrieNode(True)

    def add_word(self, word: str) -> None:
        curr_node = self.root_node
        for i, ch in enumerate(word):
            curr_node.add_child(ch, TrieNode(i == len(word) - 1))
            curr_node = curr_node.get_child(ch)

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add_word(word)

    def search_from_node(self, trie_node, word, index):
        curr_node = trie_node
        if index == len(word):
            return curr_node.is_final
        current_ch = word[index]
        if current_ch == '.':
            for child in curr_node.child_map.values():
                if self.search_from_node(child, word, index+1):
                    return True
            return False
        else:
            curr_node = curr_node.get_child(current_ch)
            if curr_node == None:
                return False
            return self.search_from_node(curr_node, word, index+1)

    def search(self, word: str) -> bool:
        return self.search_from_node(self.trie.root_node, word, 0)
