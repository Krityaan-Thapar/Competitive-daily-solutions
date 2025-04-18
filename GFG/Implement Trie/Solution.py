class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

ord_val = lambda ch: ord(ch) - ord('a')
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        curr = self.root
        for ch in word:
            idx = ord_val(ch)
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            idx = ord_val(ch)
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr.isEnd

    def isPrefix(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            idx = ord_val(ch)
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return True