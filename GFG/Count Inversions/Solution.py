class Solution:
    def inversionCount(self, arr):
        def bleh(l, r):
            count = 0
            
            if l < r:
                m = (r + l) // 2
                count += bleh(l, m)
                count += bleh(m + 1, r)
                count += merge(l, m, r)
            return count
        
        def merge(l, m, r):
            n1 = m - l + 1
            n2 = r - m
            left, right = [], []
            
            for i in range(n1):
                left.append(arr[l + i])
            for j in range(n2):
                right.append(arr[m + 1 + j])
            
            i, j, k = 0, 0, l
            count = 0
            while i < n1 and j < n2:
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    k += 1
                    i += 1
                else:
                    arr[k] = right[j]
                    k += 1
                    j += 1
                    count += n1 - i
            
            while i < n1:
                arr[k] = left[i]
                k += 1
                i += 1
            
            while j < n2:
                arr[k] = right[j]
                k += 1
                j += 1
            
            return count
        return bleh(0, len(arr) - 1)