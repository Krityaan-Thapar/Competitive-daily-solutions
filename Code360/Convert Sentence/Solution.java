import java.util.*;

public class Solution {
	public static String convertSentence(String str, int n) {
		HashMap<Character, String> keypad = new HashMap<>();
		keypad.put('a', "2");
		keypad.put('b', "22");
		keypad.put('c', "222");
		keypad.put('d', "3");
		keypad.put('e', "33");
		keypad.put('f', "333");
		keypad.put('g', "4");
		keypad.put('h', "44");
		keypad.put('i', "444");
		keypad.put('j', "5");
		keypad.put('k', "55");
		keypad.put('l', "555");
		keypad.put('m', "6");
		keypad.put('n', "66");
		keypad.put('o', "666");
		keypad.put('p', "7");
		keypad.put('q', "77");
		keypad.put('r', "777");
		keypad.put('s', "7777");
		keypad.put('t', "8");
		keypad.put('u', "88");
		keypad.put('v', "888");
		keypad.put('w', "9");
		keypad.put('x', "99");
		keypad.put('y', "999");
		keypad.put('z', "9999");

		ArrayList<String> ans = new ArrayList<>();
		for (int i = 0; i < str.length(); i++) {
			ans.add(keypad.get(str.charAt(i)));
		}

		return String.join("", ans);
	}
}