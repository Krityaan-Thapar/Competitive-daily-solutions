class Solution {
	public static char kThCharaterOfDecryptedString(String s, long k) {
		long i, j;
		long n = s.length();
		long substringLength;
		long resultantLength;
		long freqOfSubstring;
		char kThChar = '$';
		i = 0;

		while (i < n) {
			j = i;
			substringLength = 0;
			freqOfSubstring = 0;
			while (j < n && Character.isLowerCase(s.charAt((int) j))) {
				j++;
				substringLength++;
			}

			while (j < n && Character.isDigit(s.charAt((int) j))) {
				freqOfSubstring = freqOfSubstring * 10 + (s.charAt((int) j) - '0');
				j++;
			}

			resultantLength = freqOfSubstring * substringLength;
			if (k > resultantLength) {
				k -= resultantLength;
				i = j;
			} else {
				k--;
				k %= substringLength;
				kThChar = s.charAt((int) (i + k));
				break;
			}
		}
		return kThChar;
	}
}