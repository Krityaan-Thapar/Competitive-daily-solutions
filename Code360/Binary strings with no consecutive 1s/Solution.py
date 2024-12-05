from typing import List

def generateString(N: int) -> List[str]:
    ans = ['0', '1']
    for _ in range(N - 1):
        level = []
        for i in ans:
            if i[-1] == '0':
                level.append(i + '1')
            level.append(i + '0')
        ans = level
    return ans