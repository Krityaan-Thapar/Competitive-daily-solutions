import java.util.ArrayList;

public class Solution {
    private static String tab = "\t";

    public static String addTabs(int count) {
        StringBuilder tabs = new StringBuilder();
        for (int j = 0; j < count; j++) {
            tabs.append(tab);
        }

        return tabs.toString();
    }

    public static ArrayList<String> prettyJSON(String str) {
        int r = 0;
        ArrayList<StringBuilder> result = new ArrayList<StringBuilder>();
        result.add(new StringBuilder(""));
        int brace = 1;
        for (int i = 0; i < str.length(); ++i) {
            switch (str.charAt(i)) {
                case ' ':
                    continue;

                case '{':
                case '[':
                    if (brace == 1 && r == 0) {
                        result.get(r).append(str.charAt(i));
                    } else {
                        result.add(new StringBuilder(""));
                        r++;
                        result.get(r).append(addTabs(brace));
                        result.get(r).append(str.charAt(i));
                        ++brace;
                    }
                    result.add(new StringBuilder(""));
                    r++;
                    result.get(r).append(addTabs(brace));
                    break;

                case '}':
                case ']':
                    if (brace > 1) {
                        result.add(new StringBuilder(""));
                        r++;
                        result.get(r).append(addTabs(brace));
                        result.get(r).append(str.charAt(i));
                        --brace;
                    } else {
                        result.add(new StringBuilder(""));
                        r++;
                        result.get(r).append(str.charAt(i));
                        --brace;
                    }
                    break;
                case ',':
                    result.get(r).append(str.charAt(i));
                    if (str.charAt(i + 1) == '{' || str.charAt(i + 1) == '[')
                        continue;
                    else {
                        result.add(new StringBuilder(""));
                        r++;
                        result.get(r).append(addTabs(brace));
                    }
                    break;
                case ':':
                    result.get(r).append(str.charAt(i));
                    if (str.charAt(i + 1) == '{' || str.charAt(i + 1) == '[') {
                        result.add(new StringBuilder(""));
                        r++;
                        result.get(r).append(addTabs(brace));
                        i++;
                        result.get(r).append(str.charAt(i));
                        ++brace;
                        if (str.charAt(i + 1) != '{' && str.charAt(i + 1) != '[') {
                            result.add(new StringBuilder(""));
                            r++;
                            result.get(r).append(addTabs(brace));
                            i++;
                            result.get(r).append(str.charAt(i));
                        }
                    }
                    break;
                default:
                    result.get(r).append(str.charAt(i));
                    break;
            }
        }
        ArrayList<String> res = new ArrayList<>();
        for (StringBuilder sb : result) {
            res.add(sb.toString());
        }
        return res;
    }
}