import sys
sys.setrecursionlimit(10000)

# datatype term =
# | TMint of int
# | TMbtf of bool
# | TMvar of strn
# | TMlam of (strn, term)
# | TMapp of (term, term)
# | TMopr of (strn(*opr*), list(term))
# | TMif0 of (term, term, term)
# | TMfix of (strn(*f*), strn(*x*), term)

class term:
    ctag = ""
    def __str__(self):
        return ("term(" + self.ctag + ")")
# end-of-class(term)

class term_int(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMint"
    def __str__(self):
        return ("TMint(" + str(self.arg1) + ")")
# end-of-class(term_int(term))

class term_btf(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMbtf"
    def __str__(self):
        return ("TMbtf(" + str(self.arg1) + ")")
# end-of-class(term_btf(term))

class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMvar"
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")
# end-of-class(term_var(term))

class term_lam(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMlam"
    def __str__(self):
        return ("TMlam(" + self.arg1 + ";" + str(self.arg2) + ")")
# end-of-class(term_lam(term))

class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(term_app(term))

##################################################################

class term_opr(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMopr"
    def __str__(self):
        return ("TMopr(" + self.arg1 + ";" + str(self.arg2) + ")")
# end-of-class(term_opr(term))

class term_if0(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMif0"
    def __str__(self):
        return ("TMif0(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(term_if0(term))

class term_fix(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMfix"
    def __str__(self):
        return ("TMfix(" + self.arg1 + ";" + self.arg2 + ";" + str(self.arg3) + ")")
# end-of-class(term_fix(term))

##################################################################

# datatype tval =
# | TVint of int
# | TVbtf of bool
# | TVclo of (term, xenv)

class tval:
    ctag = ""
    def __str__(self):
        return ("tval(" + self.ctag + ")")
# end-of-class(tval)

class tval_int(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVint"
    def __str__(self):
        return ("TVint(" + str(self.arg1) + ")")
# end-of-class(tval_int(tval))

class tval_btf(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVbtf"
    def __str__(self):
        return ("TVbtf(" + str(self.arg1) + ")")
# end-of-class(tval_btf(tval))

class tval_clo(tval):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TVclo"
    def __str__(self):
        return ("TVclo(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(tval_clo(tval))

##################################################################

# datatype xenv =
# | EVnil of ()
# | EVcons of (strn, tval, xenv)

class xenv:
    ctag = ""
    def __str__(self):
        return ("xenv(" + self.ctag + ")")
# end-of-class(xenv)

class xenv_nil(xenv):
    def __init__(self):
        self.ctag = "EVnil"
    def __str__(self):
        return ("EVnil(" + ")")
# end-of-class(xenv_nil(xenv))

class xenv_cons(xenv):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "EVcons"
    def __str__(self):
        return ("EVcons(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(xenv_cons(xenv))

##################################################################

term_add = lambda a1, a2: term_opr("+", [a1, a2])
term_sub = lambda a1, a2: term_opr("-", [a1, a2])
term_mul = lambda a1, a2: term_opr("*", [a1, a2])
term_div = lambda a1, a2: term_opr("/", [a1, a2])
term_mod = lambda a1, a2: term_opr("%", [a1, a2])

term_lt0 = lambda a1, a2: term_opr("<", [a1, a2])
term_gt0 = lambda a1, a2: term_opr(">", [a1, a2])
term_eq0 = lambda a1, a2: term_opr("=", [a1, a2])
term_lte = lambda a1, a2: term_opr("<=", [a1, a2])
term_gte = lambda a1, a2: term_opr(">=", [a1, a2])
term_neq = lambda a1, a2: term_opr("!=", [a1, a2])
term_cmp = lambda a1, a2: term_opr("cmp", [a1, a2])

##################################################################

# #extern
# fun
# term_eval00(tm0: term): tval
# #extern
# fun
# term_eval01(tm0: term, env: envx): tval

def term_eval00(tm0):
    return term_eval01(tm0, xenv_nil())

##################################################################

def xenv_search(env, x00):
    if env.ctag == "EVnil":
        return None
    if env.ctag == "EVcons":
        if env.arg1 == x00:
            return env.arg2
        else:
            return xenv_search(env.arg3, x00)
    raise TypeError(env) # HX-2025-06-03: deadcode!

##################################################################
        
def term_eval01(tm0, env):
    # print("term_eval01: tm0 = " + str(tm0))
    if (tm0.ctag == "TMint"):
        return tval_int(tm0.arg1)
    if (tm0.ctag == "TMbtf"):
        return tval_btf(tm0.arg1)
    if (tm0.ctag == "TMlam"):
        return tval_clo(tm0, env)
    if (tm0.ctag == "TMfix"):
        return tval_clo(tm0, env)
    if (tm0.ctag == "TMvar"):
        tv0 = xenv_search(env, tm0.arg1)
        assert tv0 is not None
        return tv0
    if (tm0.ctag == "TMopr"):
        pnm = tm0.arg1
        ags = tm0.arg2 # list of arguments
        if (pnm == "+"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            # print("TMopr: tv1 = " + str(tv1))
            # print("TMopr: tv2 = " + str(tv2))
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 + tv2.arg1)
        if (pnm == "-"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 - tv2.arg1)
        if (pnm == "*"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 * tv2.arg1)
        if (pnm == "%"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 % tv2.arg1)
        if (pnm == "/"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_int(tv1.arg1 // tv2.arg1)
        if (pnm == "<"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 < tv2.arg1)
        if (pnm == ">"):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 > tv2.arg1)
        if (pnm == "="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 == tv2.arg1)
        if (pnm == "<="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 <= tv2.arg1)
        if (pnm == ">="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 >= tv2.arg1)
        if (pnm == "!="):
            assert len(ags) == 2
            tv1 = term_eval01(ags[0], env)
            tv2 = term_eval01(ags[1], env)
            assert tv1.ctag == "TVint"
            assert tv2.ctag == "TVint"
            return tval_btf(tv1.arg1 != tv2.arg1)
        raise TypeError(pnm) # HX-2025-06-03: unsupported!
    if (tm0.ctag == "TMapp"):
        tm1 = tm0.arg1
        tv1 = term_eval01(tm1, env)
        assert tv1.ctag == "TVclo"
        tm2 = tm0.arg2
        tv2 = term_eval01(tm2, env)
        tmf = tv1.arg1
        env = tv1.arg2
        if tmf.ctag == "TMlam":
            x01 = tmf.arg1
            env = xenv_cons(x01, tv2, env)
            return term_eval01(tmf.arg2, env)
        if tmf.ctag == "TMfix":
            f00 = tmf.arg1
            env = xenv_cons(f00, tv1, env)
            x01 = tmf.arg2
            env = xenv_cons(x01, tv2, env)
            return term_eval01(tmf.arg3, env)
        raise TypeError(tmf) # HX-2025-06-03: type error!
    if (tm0.ctag == "TMif0"):
        tm1 = tm0.arg1
        tv1 = term_eval01(tm1, env)
        assert tv1.ctag == "TVbtf"
        if tv1.arg1:
            return term_eval01(tm0.arg2, env) # then
        else:
            return term_eval01(tm0.arg3, env) # else
    raise TypeError(tm0) # HX-2025-05-27: should be deadcode!    

##################################################################

var_x = term_var("x")
var_y = term_var("y")
var_f = term_var("f")
var_n = term_var("n")
int_0 = term_int( 0 )
int_1 = term_int( 1 )
int_5 = term_int( 5 )
btf_t = term_btf(True)
btf_f = term_btf(False)

##################################################################

print("eval(int_1) = " + str(term_eval00(int_1)))
print("eval(btf_t) = " + str(term_eval00(btf_t)))
print("eval(int_1 + int_1) = " + str(term_eval00(term_add(int_1, int_1))))
print("eval(int_1 - int_1) = " + str(term_eval00(term_sub(int_1, int_1))))
print("eval(int_1 <= int_1) = " + str(term_eval00(term_lte(int_1, int_1))))

##################################################################

term_dbl = term_lam("x", term_add(var_x, var_x))
print("eval(term_dbl(int_1)) = " + str(term_eval00(term_app(term_dbl, int_1))))

##################################################################

int_1 = term_int( 1 )
var_f = term_var("f")
var_n = term_var("n")
int_3 = term_int( 3 )
int_5 = term_int( 5 )
int_10 = term_int(10)
term_fact = \
  term_fix("f", "n", \
    term_if0(term_lte(var_n, int_0), \
      int_1, \
      term_mul(var_n, term_app(var_f, term_sub(var_n, int_1)))))
print("eval(term_fact(int_3)) = " + str(term_eval00(term_app(term_fact, int_3))))
print("eval(term_fact(int_5)) = " + str(term_eval00(term_app(term_fact, int_5))))
print("eval(term_fact(int_10)) = " + str(term_eval00(term_app(term_fact, int_10))))

##################################################################

# HX-2025-06-04:
# Doing arithmetic in pure lambda-calculus
# What is 'two'?
# It means applying a function to its argument twice?
# What is 'three'?
# It means applying a function to its argument thrice?
# two: lam f.lam x.f(f(x)); three: lam f.lam x.f(f(f(x)))
# A 'numeral' means the representation of a number
# For instance, Roman numerals; MMXXV = 2025
# Church numeral for zero: lam f.lam x.x
# Church numeral for one: lam f.lam x.f(x)
# Church numeral for two: lam f.lam x.f(f(x))
# Church numeral for three: lam f.lam x.f(f(f(x)))

var_x = term_var("x")
var_f = term_var("f")
CHNUM0 = term_lam("f", term_lam("x", var_x))
CHNUM1 = term_lam("f", term_lam("x", term_app(var_f, var_x)))
CHNUM2 = term_lam("f", term_lam("x", term_app(var_f, term_app(var_f, var_x))))
CHNUM3 = term_lam("f", term_lam("x", term_app(var_f, term_app(var_f, term_app(var_f, var_x)))))

term_suc = term_lam("n", term_add(var_n, int_1))
def chnum_toint(chnum):
    res = term_eval00(term_app(term_app(chnum, term_suc), int_0))
    assert res.ctag == "TVint"
    return res.arg1
print("CHNUM3 = " + str(CHNUM3))
print("CHNUM3 = " + str(chnum_toint(CHNUM3)))

def int_tochnum(n0):
    assert n0 >= 0
    res = var_x
    while (n0 >= 1):
        n0 -= 1
        res = term_app(var_f, res)
    return term_lam("f", term_lam("x", res))

print("CHNUM1000 = " + str(chnum_toint(int_tochnum(1000))))

##################################################################

# HX-2025-06-04:
# Handling booleans (true and false) in pure lambda-calculus
# TMif0(tm1, tm2, tm3) = tm1(tm2)(tm3)

var_x = term_var("x")
var_y = term_var("y")
chtru = term_lam("x", term_lam("y", var_x)) # for representing true
chfls = term_lam("x", term_lam("y", var_y)) # for representing false

##################################################################
#
# chnum_suc = lam n.(lam f.lam x.n(f)(f(x)))
#
chnum_suc = \
    term_lam("n", \
      term_lam("f", \
        term_lam("x", \
          term_app(term_app(var_n, var_f), term_app(var_f, var_x)))))
#

CHNUM4 = term_app(chnum_suc, CHNUM3)
print("CHNUM4 = " + str(chnum_toint(CHNUM4)))

# def myadd(x, y):
#     if x==0:
#         return y
#     else:
#         return 1 + myadd(x-1, y)


var_m = term_var("m")
var_n = term_var("n")

#
# chnum_add =
# lam m.lam n.(lam f.lam x.m(f)(n(f)(x)))
#
chnum_add = \
  term_lam("m", term_lam("n", \
    term_lam("f", term_lam("x", \
        term_app(term_app(var_m, var_f), \
          term_app(term_app(var_n, var_f), var_x))))))

CHNUM7 = \
  term_app(\
    term_app(chnum_add, CHNUM3), CHNUM4)
print("CHNUM7 = " + str(chnum_toint(CHNUM7)))

# chnum_mul =
# lam m.lam n.(lam f.lam x.m(n(f))(x))
chnum_mul = \
  term_lam("m", term_lam("n", \
    term_lam("f", term_lam("x", \
      term_app(term_app(var_m, term_app(var_n, var_f)), var_x)))))

CHNUM49 = \
  term_app(\
    term_app(chnum_mul, CHNUM7), CHNUM7)
print("CHNUM49 = " + str(chnum_toint(CHNUM49)))

# HX-2025-06-04:
# This is what [pre_helper] does:
# (0, 0) -> (1, 0) -> (2, 1) -> (3, 2) -> ...

var_p = term_var("p")
var_t = term_var("t")

def chpair(x, y):
    return term_lam("t", term_app(term_app(var_t, x), y))

def f_chnum_pre():
    chnum_pre_helper = \
      term_lam("p", \
        chpair(term_app(chnum_suc, term_app(var_p, chtru)), term_app(var_p, chtru)))
    return \
      term_lam("n", term_app(term_app(term_app(var_n, chnum_pre_helper), chpair(CHNUM0, CHNUM0)), chfls))

chnum_pre = f_chnum_pre()

CHNUM0 = term_app(chnum_pre, CHNUM0)
print("CHNUM0 = " + str(chnum_toint(CHNUM0)))
CHNUM0 = term_app(chnum_pre, CHNUM1)
print("CHNUM0 = " + str(chnum_toint(CHNUM0)))
CHNUM1 = term_app(chnum_pre, CHNUM2)
print("CHNUM1 = " + str(chnum_toint(CHNUM1)))
CHNUM6 = term_app(chnum_pre, CHNUM7)
print("CHNUM6 = " + str(chnum_toint(CHNUM6)))
CHNUM5 = term_app(chnum_pre, CHNUM6)
print("CHNUM5 = " + str(chnum_toint(CHNUM5)))
#
# HX-2025-06-05:
# This one takes forever!!!
# CHNUM48 = term_app(chnum_pre, CHNUM49)
# print("CHNUM48 = " + str(chnum_toint(CHNUM48)))
#

chnum_gtz = \
  term_lam("n", \
    term_app(term_app(var_n, term_lam("", chtru)), chfls))

def term_if0_(tm1, tm2, tm3):
    return \
      term_app(term_app(
        term_app(tm1, term_lam("", tm2)), term_lam("", tm3)), chtru)

def term_fix_(f00, x01, tmx):
    f = term_var("f")
    x = term_var("x")
    y = term_var("y")
    fxxy = \
      term_lam("x", term_lam("y", \
        term_app(term_app(f, term_app(x, x)), y)))
    Yval = term_lam("f", term_app(fxxy, fxxy))
    return term_app(Yval, term_lam(f00, term_lam(x01, tmx)))

chnum_fact = \
  term_fix_("f", "n", \
    term_if0_(term_app(chnum_gtz, var_n), \
      term_app(term_app(chnum_mul, var_n), \
        term_app(var_f, term_app(chnum_pre, var_n))), CHNUM1))

print("chnum_fact(0) = " + str(chnum_toint(term_app(chnum_fact, CHNUM0))))
print("chnum_fact(3) = " + str(chnum_toint(term_app(chnum_fact, CHNUM3))))
print("chnum_fact(5) = " + str(chnum_toint(term_app(chnum_fact, CHNUM5))))
print("chnum_fact(7) = " + str(chnum_toint(term_app(chnum_fact, CHNUM7))))

##################################################################

def term_comp00(tm0):
    if tm0.ctag == "TMint":
        n00 = tm0.arg1
        assert n00 >= 0
        return int_tochnum(n00)
    if tm0.ctag == "TMbtf":
        btf = tm0.arg1
        return chtru if btf else chfls
    if tm0.ctag == "TMvar":
        x01 = tm0.arg1
        return term_var(x01)
    if tm0.ctag == "TMlam":
        x01 = tm0.arg1
        tmx = tm0.arg2
        return term_lam(x01, term_comp00(tmx))
    if tm0.ctag == "TMapp":
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        return term_app(term_comp00(tm1), term_comp00(tm2))
    if tm0.ctag == "TMfix":
        f00 = tm0.arg1
        x01 = tm0.arg2
        tmx = tm0.arg3
        return term_fix_(f00, x01, term_comp00(tmx))
    if tm0.ctag == "TMif0":
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        tm3 = tm0.arg3
        return term_if0_(term_comp00(tm1), term_comp00(tm2), term_comp00(tm3))
    #
    # Please try to handle TMopr on your own!
    #
    raise TypeError(tm0) # HX-2025-06-05: deadcode!

##################################################################

##################################################################
# end of [CS391-2025-Summer/assigns/02/Solution/assign0y.py
##################################################################
