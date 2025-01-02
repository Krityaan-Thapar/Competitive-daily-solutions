class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        
        n = len(word)
        ans = ""
        best_l = n - numFriends + 1
        for i in range(n):
            cand = word[i:min(i + best_l, n)]
            if cand > ans:
                ans = cand
        return ans