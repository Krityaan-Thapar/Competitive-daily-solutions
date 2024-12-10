class Solution:
    def maximumLength(self, s: str) -> int:
        chain = 0
        prev = None
        store = [[-1 for _ in range(3)] for _ in range(26)]

        for char in s:
            if char == prev:
                chain += 1
            else:
                chain = 1
                prev = char

            ascii_val = ord(char) - ord('a')
            if chain > store[ascii_val][0]:
                store[ascii_val][2] = store[ascii_val][1]
                store[ascii_val][1] = store[ascii_val][0]
                store[ascii_val][0] = chain
            elif chain > store[ascii_val][1]:
                store[ascii_val][2] = store[ascii_val][1]
                store[ascii_val][1] = chain
            elif chain > store[ascii_val][2]:
                store[ascii_val][2] = chain

        ans = -1
        for i in range(26):
            ans = max(ans, min(store[i]))
        return ans