from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        ans = 0

        for i in freq:
            if freq[i] >= 3:
                if freq[i] % 2 == 0:
                    ans += 2
                else:
                    ans += 1
            else:
                ans += freq[i]
        return ans

class Solution2:
    def minimumLength(self, s: str) -> int:
        return sum(2 if x % 2 == 0 else 1 for x in Counter(s).values())

obj = Solution()
print(obj.minimumLength("abaacbcbb"))
print(obj.minimumLength("aa"))