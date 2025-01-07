from collections import Counter
class Solution:
    def countPairs (self, arr, target):
        freq = Counter(arr)
        seen = set()
        
        ans = 0
        for i in freq:
            req = target - i
            if i == req:
                x = freq[i]
                ans += ((x * (x - 1)) // 2)
            elif req not in seen:
                ans += (freq[i] * freq[req])
                seen.add(i)
        return ans

class Solution2:
    def countPairs (self, arr, target):
        i, j = 0, len(arr) - 1
        
        ans = 0
        while i < j:
            s = arr[i] + arr[j]
            if s == target:
                if arr[i] == arr[j]:
                    x = j - i + 1
                    ans += ((x * (x - 1)) // 2)
                    break
                
                x, y = 1, 1
                while arr[i] == arr[i + 1]:
                    i += 1
                    x += 1
                while arr[j] == arr[j - 1]:
                    j -= 1
                    y += 1
                ans += x * y
                i += 1
                j -= 1
            elif s < target:
                i += 1
            else:
                j -= 1
        return ans