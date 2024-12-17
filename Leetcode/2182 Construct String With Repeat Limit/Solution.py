class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0 for _ in range(26)]
        for i in s:
            ord_val = ord(i) - ord('a')
            freq[ord_val] += 1
        
        ans = []
        ptr1 = 25
        ptr2 = 25

        while ptr1 >= 0 and ptr2 >= 0:
            while freq[ptr1] == 0:
                ptr1 -= 1
            while ptr2 >= ptr1 or freq[ptr2] == 0:
                ptr2 -= 1
            
            if ptr1 < 0 or ptr2 < 0:
                break
            chr1 = chr(ptr1 + ord('a'))
            chr2 = chr(ptr2 + ord('a'))

            if ans and ans[-1][-1] == chr1:
                if len(ans[-1]) < repeatLimit:
                    insert_freq = min(freq[ptr1], repeatLimit - len(ans[-1]))
                    freq[ptr1] -= insert_freq
                    ans[-1] = chr1 * (len(ans[-1]) + insert_freq)
                else:
                    freq[ptr2] -= 1
                    ans.append(chr2)
            else:
                insert_freq = min(freq[ptr1], repeatLimit)
                freq[ptr1] -= insert_freq
                ans.append(chr1 * insert_freq)
        
        if freq[ptr1] > 0:
            chr1 = chr(ptr1 + ord('a'))
            if not ans:
                ans.append(chr1 * min(repeatLimit, freq[ptr1]))
            elif ans[-1][-1] != chr1:
                ans.append(chr1 * min(repeatLimit, freq[ptr1]))
            elif len(ans[-1]) < repeatLimit:
                ans[-1] = ans[-1] + chr1 * min(freq[ptr1], repeatLimit - len(ans[-1]))
        return "".join(ans)