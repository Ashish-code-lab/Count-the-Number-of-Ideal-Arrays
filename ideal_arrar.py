class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        MOD = 10**9 + 7
        fact = [1] * (n + 1)
        invfact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def nCr(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD
        maxLen = maxValue.bit_length()     
        dp = [[0] * (maxLen + 1) for _ in range(maxValue + 1)]
        for v in range(1, maxValue + 1):
            dp[v][1] = 1
        for k in range(1, maxLen):
            for v in range(1, maxValue + 1):
                if dp[v][k]:
                    for m in range(v * 2, maxValue + 1, v):
                        dp[m][k + 1] = (dp[m][k + 1] + dp[v][k]) % MOD
        ans = 0
        for k in range(1, maxLen + 1):
            chains_k = sum(dp[v][k] for v in range(1, maxValue + 1)) % MOD
            ans = (ans + chains_k * nCr(n - 1, k - 1)) % MOD

        return ans
