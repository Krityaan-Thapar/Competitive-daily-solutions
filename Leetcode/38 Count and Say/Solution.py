class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        for _ in range(1, n):
            nex = []
            prev = None
            for ch in curr:
                if prev is None:
                    prev = [1, ch]
                    continue
                
                if ch != prev[1]:
                    nex.append(str(prev[0]))
                    nex.append(prev[1])
                    prev = [1, ch]
                else:
                    prev[0] += 1
            nex.append(str(prev[0]))
            nex.append(prev[1])
            curr = "".join(nex)
        return curr