class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sl, st = len(start), len(target)
        idx1, idx2 = 0, 0

        while idx1 < sl or idx2 < st:
            while idx1 < sl and start[idx1] == "_":
                idx1 += 1
            
            while idx2 < st and target[idx2] == "_":
                idx2 += 1
            
            if idx1 == sl or idx2 == st:
                return idx1 == sl and idx2 == st
            
            if start[idx1] != target[idx2] or (start[idx1] == 'L' and idx1 < idx2) or (start[idx1] == 'R' and idx1 > idx2):
                return False

            idx1 += 1
            idx2 += 1
        return True 