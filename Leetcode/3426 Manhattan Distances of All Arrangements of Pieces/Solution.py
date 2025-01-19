MOD = int(1e9) + 7
MOD2 = int(1e9) + 5
def fast_pow(x, y):
    x = x % MOD
    ans = 1
    
    while y > 0:
        if y % 2 == 1:
            ans = (ans * x) % MOD
        x = (x * x) % MOD
        y = y // 2
    return ans

fact = [0 for _ in range(int(1e5 + 1))]
inv_fact = [0 for _ in range(int(1e5 + 1))]
fact[0] = 1
for i in range(1, int(1e5) + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[-1] = fast_pow(fact[-1], MOD2)
for i in range(int(1e5) - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def comb(n, k):
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        if k <= 1:
            return 0

        squares = m * n
        a = comb(squares - 2, k - 2)
        sum_sq_m = m * (m - 1) * (m + 1) // 6 % MOD
        sum_sq_n = n * (n - 1) * (n + 1) // 6 % MOD
        s = (sum_sq_m * n * n % MOD) + (sum_sq_n * m * m % MOD)
        return a * s % MOD