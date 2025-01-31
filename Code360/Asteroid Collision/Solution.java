import java.util.*;

public class Solution {
    public static List< Integer > collidingAsteroids(int []asteroids) {
        Stack<Integer> stk = new Stack<Integer>();
        List<Integer> ans = new ArrayList<>();
        
        for (int i = 0; i < asteroids.length; i++) {
            int curr = asteroids[i];
            if (stk.size() == 0 && curr == 0) {
                ans.add(curr);
                continue;
            }

            if (curr < 0) {
                boolean destroy = false;
                while (stk.size() > 0) {
                    if (stk.peek() < -1 * curr) {
                        stk.pop();
                    } else if (stk.peek() == -1 * curr) {
                        destroy = true;
                        stk.pop();
                        break;
                    } else {
                        destroy = true;
                        break;
                    }
                }

                if (!destroy) {
                    ans.add(curr);
                }
            } else {
                stk.add(curr);
            }
        }
        
        Stack<Integer> reverser = new Stack<Integer>();
        while (stk.size() > 0) {
            if (stk.peek() == 0) {
                stk.pop();
                continue;
            }
            reverser.add(stk.pop());
        }
        while (reverser.size() > 0) {
            ans.add(reverser.pop());
        }
        return ans;
    }
}