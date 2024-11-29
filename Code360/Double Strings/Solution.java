import java.util.HashSet;

public class Solution {
    private static long fastPow(long base, long power) {
        long res = 1;
        long m = (int) 1e9 + 7;
        while (power > 0) {
            if ((power & 1) != 0) {
                res = res * base;
                res %= m;
            }
            base *= base;
            base %= m;
            power >>= 1;
        }
        return res;
    }

    private static long createHashValue(String str, long n) {
        long result = 0;
        long m = (int) 1e9 + 7;
        long prime = 31;
        for (int i = 0; i < n; i++) {
            result += (long) ((long) str.charAt(i) * fastPow(prime, i));
            result %= m;
        }
        return result;
    }

    private static long recalculateHash(char old, char newC, long oldHash, long patLength) {
        long newHash;
        long prime = 31;
        long m = (int) 1e9 + 7;
        newHash = oldHash - (long) old;
        newHash *= fastPow(prime, m - 2);
        newHash += ((long) newC * fastPow(prime, patLength - 1));
        newHash %= m;
        return newHash;
    }

    public static int findDoubleStrings(String str) {
        int n = str.length();
        HashSet<Long> ans = new HashSet<Long>();
        for (int i = 2; i <= n; i += 2) {
            String temp = "";
            for (int j = 0; j < i / 2; j++) {
                temp += str.charAt(j);
            }

            long hash1 = createHashValue(temp, i / 2);
            temp = "";
            for (int j = i / 2; j < i; j++) {
                temp += str.charAt(j);
            }

            long hash2 = createHashValue(temp, i / 2);
            for (int s1 = 0, e1 = i / 2, s2 = i / 2, e2 = i; e2 < n; s1++, s2++, e1++, e2++) {
                if (hash1 == hash2) {
                    ans.add(hash1);
                }

                hash1 = recalculateHash(str.charAt(s1), str.charAt(e1), hash1, i / 2);
                hash2 = recalculateHash(str.charAt(s2), str.charAt(e2), hash2, i / 2);
            }

            if (hash1 == hash2) {
                ans.add(hash1);
            }
        }

        return ans.size();

    }
}