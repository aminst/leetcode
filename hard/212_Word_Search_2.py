class TrieNode:
    def __init__(self):
        self.char_to_node = dict()
        self.is_final = False
        self.word = None
    
    def set_final(self):
        self.is_final = True
    
    def set_word(self, word):
        self.word = word
    
    def add_node(self, char):
        self.char_to_node[char] = TrieNode()

    def get_node(self, char):
        return self.char_to_node[char]
    
    def has_char(self, char):
        return char in self.char_to_node

class Trie:
    def __init__(self):
        self.head = TrieNode()     

    def add_word(self, word):
        curr = self.head
        for char in word:
            if not curr.has_char(char):
                curr.add_node(char)
            curr = curr.get_node(char)
        curr.set_final()
        curr.set_word(word)


class Solution:
    def __init__(self):
        self.found_words = set()

    def find_words(self, x, y, board, curr_trie_node, used_pos):
        if curr_trie_node.is_final:
            self.found_words.add(curr_trie_node.word)
        if x < 0 or x == len(board) or y < 0 or y == len(board[0]): return

        if curr_trie_node.has_char(board[x][y]) and (x, y) not in used_pos:
            used_pos.add((x, y))
            self.find_words(x + 1, y, board, curr_trie_node.get_node(board[x][y]), used_pos)
            self.find_words(x - 1, y, board, curr_trie_node.get_node(board[x][y]), used_pos)
            self.find_words(x, y + 1, board, curr_trie_node.get_node(board[x][y]), used_pos)
            self.find_words(x, y - 1, board, curr_trie_node.get_node(board[x][y]), used_pos)
            used_pos.remove((x, y))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            t.add_word(word)
        
        for i, row in enumerate(board):
            for j, el in enumerate(row):
                self.find_words(i, j, board, t.head, set())
        
        return list(self.found_words)
