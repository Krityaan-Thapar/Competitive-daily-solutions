class Solution:
    def productExceptSelf(self, arr):
        p = 1
        c_z = 0
        
        for i in arr:
            if i == 0:
                c_z += 1
            else:
                p *= i
        
        if c_z >= 2:
            return [0 for _ in range(len(arr))]
        elif c_z == 1:
            return [p if i == 0 else 0 for i in arr]
        else:
            return [p // i for i in arr]