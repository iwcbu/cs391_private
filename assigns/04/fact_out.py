import lambda2

"""
/* ****** ****** */
#include <stdio.h>
#include "runtime.h"

/* ****** ****** */

extern
void*
mymalloc(size_t n) {
  void* p0;
  p0 = malloc(n);
  if (p0 != 0) return p0;
  fprintf(stderr, "myalloc failed!!!\n");
  exit(1);
}

/* ****** ****** */

"""
# python already does this
########################################

"""
extern
void
LAMVAL_print(lamval1 x)
{
  int tag;
  tag = x->tag;
  switch( tag )
  {
    case TAGcfp:
      printf("<lamval1_cfp>"); break;
    case TAGint:
      printf("%i", ((lamval1_int)x)->data); break;
    case TAGstr:
      printf("%s", ((lamval1_str)x)->data); break;
    default: printf("Unrecognized tag = %i", tag);
  }
}

/* ****** ****** */
"""
def LAMVAL_print(x):
    ctag = x.ctag
    if ctag == "TVint":
        print(x.arg1, end="")
    elif ctag == "TVbtf":
        print(x.arg1, end="")
    elif ctag == "TVclo":
        print("<closure>", end="")
    elif ctag == "TVtup":
        v1, v2 = x.arg1
        print("(", end="")
        LAMVAL_print(v1)
        print(", ", end="")
        LAMVAL_print(v2)
        print(")", end="")
    else:
        assert ValueError(f"Unrecognized ctag: {ctag}", end="")

"""
/*
fun
fact(x) = if x > 0 then x * fact(x-1) else 1
*/

/* ****** ****** */

lamval1
fact(lamval1 arg1)
{

  lamval1 ret0;
  lamval1 tmp1, tmp2, tmp3, tmp4;

  tmp1 = LAMOPR_igt(arg1, LAMVAL_int(0));

  if (((lamval1_int)tmp1)->data) {
    tmp2 = LAMOPR_sub(arg1, LAMVAL_int(1));
    tmp3 = fact(tmp2);
    ret0 = LAMOPR_mul(arg1, tmp3);
  } else {
    ret0 = LAMVAL_int(1);
  }

  return ret0;
}
"""

def fact(x):
    # fact(x) = if x > 0 then x * fact(x-1) else 1

    # x is of type styp_int
    tp = lambda2.term_tpck00(x)
    if not lambda2.styp_equal(tp, lambda2.styp_int):
        #if the input is not an integer
        raise TypeError(f"fact:  expected int input, but x is of type {tp}")
    
    # x > 0
    test = lambda2.term_eval00(lambda2.term_gt0(x, lambda2.int_0))
    if test.ctag != "TVbtf":
        #if test is not a bool
        raise TypeError(f"fact:  expected test to be bool, but test is of type {test.ctag}")
    
    #if x > 0
    if test.arg1:

        # def x as a term value n
        n = lambda2.term_eval00(x)
        if n.ctag != "TVint":
            raise TypeError(f"fact: expected n to be TVint, but n is of type {n.ctag}")
        n = n.arg1

        # fact(x - 1)
        prev = fact(lambda2.term_int(n-1))
        if prev.ctag != "TVint":
            raise TypeError(f"fact: expected prev to be TVint, but n is of type {prev.ctag}")
        
        # x * fact(x - 1)
        return lambda2.tval_int(n * prev)
    else:
        return lambda2.tval_int(1)

"""
int main() {
  LAMVAL_print(fact(LAMVAL_int(10))); printf("\n"); return 0;
}
"""

LAMVAL_print(fact(lambda2.term_int(10)))

