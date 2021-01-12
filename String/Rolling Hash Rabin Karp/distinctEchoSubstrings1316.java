import java.math.*;
public class Solution {
	private int R = 256; // radix
	private long Q; // large prime
	private long[] powers; // precomputed powers of R
	private long[] hashes; // precomputed hashes of prefixes

	public int distinctEchoSubstrings(String s) {
		Set<Long> set = new HashSet<>();
		preprocess(s.length(), s);

		for (int len = 1; len <= s.length() / 2; len++) {
			for (int l = 0, r = len, count = 0; l < s.length() - len; l++, r++) {
				if (s.charAt(l) == s.charAt(r)) count++;
				else count = 0;

				if (count == len) {
					set.add(getHash(l - len + 1, l + 1));
					count--;
				}
			}
		}

		return set.size();
	}

	private void preprocess(int n, String text) {
		Q = calculateRandomPrime();
		hashes = new long[n + 1];
		powers = new long[n + 1];
		powers[0] = 1;
		for (int i = 1; i <= n; i++) {
			hashes[i] = (hashes[i - 1] * R + text.charAt(i - 1)) % Q;
			powers[i] = (powers[i - 1] * R) % Q;
		}
	}

	private long calculateRandomPrime() {
		BigInteger prime = BigInteger.probablePrime(31, new Random());
		return prime.longValue();
	}

	private long getHash(int l, int r) {
		return (hashes[r] + Q - hashes[l] * powers[r - l] % Q) % Q;
	}
}


// https://leetcode.com/problems/distinct-echo-substrings/discuss/492704/Intuitive100-Sliding-Window-Rolling-Counter-(with-pictures)
class Solution {
    public int distinctEchoSubstrings(String s) {
        // brute force O(n^2)
        Set<String> set = new HashSet<>();
        int n = s.length();
        for (int len = 1; len <= n / 2; len++) {
            for (int l = 0, r = len, count = 0; l < n - len; l++, r++) {
                if (s.charAt(l) == s.charAt(r)) count++;
                else count = 0;
                if (count == len) {
                    set.add(s.substring(l - len + 1, l + 1));
                    count--;
                }
            }
        }
        return set.size();
    }
}