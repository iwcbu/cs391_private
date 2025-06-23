# Assignment 3 for CS391X1, Summer I, 2025

## Total points: 100

## Description of the task

Please first study the code in the following directory
where a simple type-checker for some extended lambda-calculus:

- lectures/lecture-06-10: pure type-checking for LAMBDA

### Task 1

Please extend the code in `lecture-06-10/lambda2.py` to handle
addtion languge constructs `TMlet`, `TMfst`, `TMsnd`, and `TMtup`:

```
datatype term =
//
| TMint of int
| TMbtf of bool
//
| TMvar of strn
| TMlam of (strn, styp, term)
| TMapp of (term, term)
//
| TMopr of (strn(*opr*), list(term))
| TMif0 of (term, term, term)
| TMfix of (strn(*f*), strn(*x*), styp, styp, term)
//
// HX-2025-06-10:
// for handling tuples of length 2:
| TMfst of term // first projection
| TMsnd of term // second projection
| TMtup of (term, term) // tuple construction
//
// HX-2025-06-10:
// for (let x = t1 in t2), which stands for
// (lam x. t1)(t2):
// TMlet of (strn(*x*), term(*t1*), term(*t2))
//
```
This part is worth 80 points.

### Task 2

Please annotate the following term with types for
bound variables:

```
# chnum_mul =
# lam m.lam n.(lam f.lam x.m(n(f))(x))
chnum_mul = \
  term_lam("m", term_lam("n", \
    term_lam("f", term_lam("x", \
      term_app(term_app(var_m, term_app(var_n, var_f)), var_x)))))
```

For receiving full credit (20 points), your annotated version of
`chnum_mul` must be able to pass the simple type-checking implemented
during lecture-06-10.  If you are not clear as to what type annotation
means, please study the examples `term_dbl` and `term_fact` presented
during lecture-06-10.

### Submission

You are expected to have all of your submitted code in one file of
the name `assign03.py`; this file should be stored in the directory
of the name `assigns/03/MySolution`. Please visit the following page
for information on creating a private repository of your own for this
class:

```
https://github.com/hwxi/CS391-2025-Summer/blob/main/README.md
```
