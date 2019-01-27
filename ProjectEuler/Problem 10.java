// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

// Find the sum of all the primes below two million.

class Main {
  public static void main(String[] args) {
    int bound = 2000000;
    long sum = 0;
    for (int i = 2; i < bound; i++) {
      if (isPrime(i)) {
        sum += i;
      }
    }
    System.out.println(sum);
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
