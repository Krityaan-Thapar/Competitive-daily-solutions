from typing import List

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for idx, i in enumerate(words):
            if i.startswith(searchWord):
                return idx + 1
        return -1