public class Main {
  public static void main(String[] args) {
    int biggest = 1;
    for (int i = 999; i > 99; i--) {
      for (int j = 999; j > 99; j--) {
        if (isPalindrome(i * j) && i * j > biggest) {
          biggest = i * j;
        }
      }
    }
    System.out.println(biggest);
  }

  public static boolean isPalindrome(int n) {
    String s = n + "";
    if (s.length() % 2 == 1 && s.substring(0, s.length() / 2).equals(reverse(s.substring(s.length() / 2 + 1)))) {
      return true;
    } else if (s.length() % 2 == 0 && s.substring(0, s.length() / 2).equals(reverse(s.substring(s.length() / 2)))) {
      return true;
    } else {
      return false;
    }
  }

  public static String reverse(String s) {
    if (s.length() == 1) {
      return s;
    } else {
      return s.substring(s.length() - 1) + reverse(s.substring(0, s.length() - 1));
    }
  }
}
