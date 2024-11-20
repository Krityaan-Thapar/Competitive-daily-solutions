from collections import deque

def createSequence(n):
    q = deque([2, 5])
    ans = []

    while q:
        curr = q.popleft()
        if curr <= n:
            ans.append(curr)
            q.append(curr * 10 + 2)
            q.append(curr * 10 + 5)
    return ans
