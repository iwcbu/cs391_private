# Quiz 1 for CS391X1, Summer I, 2025

## Date: Friday, the 30th of May, 2025

## How to submit?

Please submit into the folder `Quiz01` on
the Gradescope page for this class.

## Question 1 (10 points)

The following function `fibo` computes Fibonacci numbers:

```
def fibo(n):
  return n if n <= 1 else fibo(n-1)+fibo(n-2)
```

Please represent `fibo` as a lambda-term in Church's lambda-calculus
extended with integers, booleans, if-then-else, and some arithmetic
operations. You can find more details on this extension in
`lectures/lecture-05-28/lambda1.dats`.
  
## Question 2 (20 points)

Please implement a function `isPrime` in Python that tests whether a
given integer is a prime number or not. Then represent _your
implementation_ of `isPrime` as a lambda-term in the same extended
lambda-calculus.

## Question 3 (100 points)

Please extend the implementation of `term_subst` in `lambda0.py`
(located in the directory `lectures/lecture-05-27`) to handle the
additional cases `TMint`, `TMbtf`, `TMif0`, and `TMopr`, which are
present in the extended lambda-calculus used in `lambda1.dats`.
