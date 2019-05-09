#include <stdio.h>
#include <math.h>

/*Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately
to the left of 3/7.
*/

// The question is essentially asking to find the fraction closest to and less than 3/7 with a denominator of less than one million.
// I initially started with denominator 2 and working my way up but I realized that I should have worked backwards, but it was too late
// (sunk cost fallacy ha). Then the program stopped near the end so I picked up where I left off.

int main(void) {
  double ts = 3.0 / 7.0;
  double eps = ts;
  double ans  = 1;
  int mil = 1000000;


  for (double d = 999983; d <= mil; d++) {
    for (double n = 428564; n < d / 2; n++) {
      if (ts - (n / d) < eps && ts - n / d > 0) {
        eps = ts - n / d;
        ans = n;
      }
    }
  }
  printf("%f", ans);
  return 0;
}
