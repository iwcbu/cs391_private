# Midterm 1 for CS391X1, Summer I, 2025

## Date: Friday, the 10th of June, 2025

## How to submit?

Please submit into the folder `Midterm` on the Gradescope page for
this class. All of your submitted code should be stored in a file of
the name `midterm.py` located in the director `midterm/01/MySolution`.

## Description of the task

### Task 1

In the following file, you can find a solution to the famous
8-queen puzzle:

```
https://ats-lang.sourceforge.net/DOCUMENT/INT2PROGINATS/HTML/x631.html
```

The solution is written in ML-like syntax. Task 1 asks you to
_translate_ this solution into LAMBDA, the extended lambda-calculus
described in `assigns/03`:


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
| TMlet of (strn(*x*), term(*t1*), term(*t2))
//
```

Task 1 is worth 200 points.

### Task 2

Your translation (written in LAMBDA) is
expected to run under an interpreter for the extended lambda-calculus.
However, this interpreter is not yet available and you need to implement
it on your own. You can and probably should base your implementation of
this interpreter on `lecture-06-04/lambda1.py`. Task 2 is worth 100 points.
