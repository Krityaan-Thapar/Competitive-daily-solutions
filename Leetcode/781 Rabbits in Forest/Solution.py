from math import ceil
from typing import List
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer_freq = Counter(answers)
        result = 0
        for ans, count in answer_freq.items():
            result += ceil(count / (ans + 1)) * (ans + 1)
        return result