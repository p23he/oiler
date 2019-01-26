// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

class Main {
  public static void main(String[] args) {
    int smallest = 1;
    loop: for (int i = 20; true; i++) {
      for (int j = 20; j > 0; j--) {
        if (i % j != 0) {
          break;
        }
        if (j == 1) {
          smallest = i;
          break loop;
        }
      }
    }
    System.out.println(smallest);
  }
}
