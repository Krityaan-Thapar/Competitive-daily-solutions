import java.util.Stack;

public class Solution{
    static class Queue {
        Stack<Integer> st;

        Queue() {
            st = new Stack<Integer>();
        }

        void enQueue(int val) {
            st.push(val);
        }

        int deQueue() {
            if (st.isEmpty()) {
                return -1;
            }

            int x = st.peek();
            st.pop();

            if (st.isEmpty()) {
                return x;
            }

            int nxt = deQueue();
            st.push(x);
            return nxt;
        }

        int peek() {
            if (st.isEmpty()) {
                return -1;
            }
            
            int x = st.peek();
            st.pop();
            
            if (st.isEmpty()) {
                st.push(x);
                return x;
            }
            
            int nxt = peek();
            st.push(x);
            return nxt;
        }

        boolean isEmpty() {
            return (st.isEmpty());
        }
    }
}