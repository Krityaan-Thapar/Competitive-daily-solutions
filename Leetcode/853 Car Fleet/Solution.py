from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = [(position[i], speed[i]) for i in range(len(position))]
        zipped.sort(reverse = True)

        stk = []
        for p, s in zipped:
            if stk and s > stk[-1][1]:
                cmp_p, cmp_s = stk[-1][0], stk[-1][1]
                f_time_to_target = (target - cmp_p) / cmp_s
                s_time_to_target = (target - p) / s
                if s_time_to_target > f_time_to_target:
                    stk.append([p, s])
            else:
                stk.append([p, s])
        return len(stk)