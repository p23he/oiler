// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

// What is the 10 001st prime number?

import java.util.*;

public class Main {
  public static void main(String[] args) {
    int n = 10001;
    ArrayList<Integer> l = new ArrayList<Integer>();
    for (int i = 2; l.size() != n; i++) {
      if (isPrime(i)) {
        l.add(i);
      }
    }
    System.out.println(l.get(l.size() - 1));
  }

  public static boolean isPrime(int p) {
    boolean prime = true;
    for (int i = 2; i <= Math.sqrt(p); i++) {
      if (p % i == 0) {
        prime = false;
      }
    }
    return prime;
  }
}
