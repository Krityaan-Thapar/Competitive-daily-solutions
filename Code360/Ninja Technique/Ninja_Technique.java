public class Ninja_Technique {
    public static boolean ninjaTechnique(String str) {
        for (int i = 0; i < str.length(); i++) {
            int local = 0;
            for (int j = i; j < str.length(); j++) {
                local *= 10;
                local += str.charAt(j) - '0';

                if (local <= 1) {
                    continue;
                }

                double sq = Math.sqrt(local);
                int c = (int) Math.ceil(sq);
                int f = (int) Math.floor(sq);
                if (c != f && c * f == local) {
                    return true;
                }
            }
        }

        return false;
    }
}