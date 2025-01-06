from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0 for _ in range(n)]

        for idx, i in enumerate(boxes):
            if i == '0':
                continue
            for x in range(n):
                ans[x] += abs(idx - x)
        return ans

class Solution2:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0 for _ in range(n)]

        left_cnt, left_move = 0, 0
        right_cnt, right_move = 0, 0
        for i in range(n):
            ans[i] += left_move
            left_cnt += int(boxes[i])
            left_move += left_cnt

            j = n - i - 1
            ans[j] += right_move
            right_cnt += int(boxes[j])
            right_move += right_cnt
        return ans