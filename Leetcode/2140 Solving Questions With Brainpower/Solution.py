from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        Q = len(questions)
        cache = [-1 for _ in range(Q)]

        def solver(idx):
            if idx >= Q:
                return 0
            
            if cache[idx] != -1:
                return cache[idx]
            
            # take
            take = questions[idx][0] + solver(idx + questions[idx][1] + 1)
            # no-take
            no_take = solver(idx + 1)
            cache[idx] = max(take, no_take)
            return cache[idx]
        return solver(0)