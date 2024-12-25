import java.util.* ;

public class Solution {
  public static Queue<Integer> reverseQueue(Queue<Integer> q) {
    Stack<Integer> stk = new Stack<Integer>();
    
    while(q.size() > 0) {
      stk.add(q.poll());
    }

    while(stk.size() > 0) {
      q.add(stk.pop());
    }
    return q;
  }
}