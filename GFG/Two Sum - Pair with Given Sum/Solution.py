class Solution:
    def twoSum(self, arr, target):
        seen = set()
        for i in arr:
            if target - i in seen:
                return True
            seen.add(i)
        return False