/* ****** ****** */

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

extern
lamval1
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

/*
fun
fact2(n) =
let
  fun
  helper(i, r) =
    if i < n
    then helper(i+1, (i+1)*r) else r
in//let
  helper(0, 1)
end//let
*/

/* ****** ****** */

extern
lamval1
fact2(lamval1 arg1);

extern
lamval1
helper
(lamval1 arg1, lamval1 arg2, lamval1 env1);

lamval1
fact2(lamval1 arg1) // arg1 is [n]
{
  lamval1 ret0;
  ret0 = helper(LAMVAL_int(0), LAMVAL_int(1), arg1);
  return ret0;
}

lamval1
helper
( lamval1 arg1
, lamval1 arg2
, lamval1 env1) {
  // arg1 is [i] // arg2 is[r] // env1 is [n]
  lamval1 ret0;
  lamval1 tmp1, tmp2, tmp3, tmp4;
  tmp1 = LAMOPR_ilt(arg1, env1);
  if (((lamval1_int)tmp1)->data) {
    tmp2 = LAMOPR_add(arg1, LAMVAL_int(1));
    tmp3 = LAMOPR_add(arg1, LAMVAL_int(1));
    tmp4 = LAMOPR_mul(tmp3, arg2);
    ret0 = helper(tmp2, tmp4, env1);
  } else {
    ret0 = arg2;
  }
  return ret0;
}

int main() {
  LAMVAL_print(fact2(LAMVAL_int(10))); printf("\n"); return 0;
}
