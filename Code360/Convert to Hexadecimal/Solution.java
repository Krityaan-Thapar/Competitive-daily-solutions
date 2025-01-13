import java.util.* ;

public class Solution {
	public static String toHex(int num) {
		HashMap<Long, String> m = new HashMap<>();
		for (long i = 0L; i <= 9L; i++) {
			m.put(i, Long.toString(i));
		}

		char x = 'A';
		for (long i = 10L; i <= 15L; i++) {
			m.put(i, Character.toString(x));
			x += 1;
		}

		StringBuilder result = new StringBuilder();
		long tmp = 0L;
		if (num < 0) {
			tmp = (long) (Math.pow(16, 8) + num);
		} else {
			tmp = (long) num;
		}

		while (tmp > 0) {
			long d = tmp % 16;
			result.append(m.get(d));
			tmp = tmp / 16;
		}
		
		return result.reverse().toString();
	}
}