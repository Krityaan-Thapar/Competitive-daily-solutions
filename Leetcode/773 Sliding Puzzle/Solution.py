from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        compress = [0 for _ in range(6)]
        for i in range(2):
            for j in range(3):
                compress[i * 3 + j] = board[i][j]
        
        def isSolved(compress):
            for i in range(6):
                if compress[i] != (i + 1) % 6:
                    return False
            return True
        
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()
        q = deque([tuple(compress)])
        moves = 0
        while q:
            q_len = len(q)
            next_level = deque([])
            for _ in range(q_len):
                curr = q.popleft()
                if curr in visited:
                    continue
                
                visited.add(curr)
                if isSolved(curr):
                    return moves
                
                l = list(curr)
                z_pos = -1
                for i in range(6):
                    if l[i] == 0:
                        z_pos = i
                        zx, zy = i // 3, i % 3
                        break
                
                for dx, dy in d:
                    nx, ny = zx + dx, zy + dy
                    if 0 <= nx < 2 and 0 <= ny < 3:
                        pos = nx * 3 + ny
                        l[pos], l[z_pos] = l[z_pos], l[pos]
                        next_level.append(tuple(l))
                        l[pos], l[z_pos] = l[z_pos], l[pos]
            q = next_level
            moves += 1
        return -1