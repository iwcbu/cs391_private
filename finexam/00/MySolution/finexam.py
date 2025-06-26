##################################################################
import sys
sys.setrecursionlimit(10000)
##################################################################

# datatype styp =
# | STbas of strn # int, bool, ...
# | STtup of (styp, styp) # for pairs
# | STfun of (styp, styp) # for functions

class styp:
    ctag = ""
    def __str__(self):
        return ("styp(" + self.ctag + ")")
# end-of-class(styp)

# | STbas of strn # int, bool, ...
class styp_bas:
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "STbas"
    def __str__(self):
        return ("STbas(" + self.arg1 + ")")
# end-of-class(styp_bas(styp))

styp_int = styp_bas("int")
styp_bool = styp_bas("bool")

# | STtup of (styp, styp) # for pairs
class styp_tup:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "STtup"
    def __str__(self):
        return ("STtup(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(styp_tup(styp))

styp_int2 = styp_tup(styp_int, styp_int)

# | STfun of (styp, styp) # for functions
class styp_fun:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "STfun"
    def __str__(self):
        return ("STfun(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(styp_fun(styp))

styp_fun_int_int = styp_fun(styp_int, styp_int)

class styp_let:
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "STlet"
    def __str__(self):
        return ("STlet(" + str(self.arg1) + "; " + str(self.arg2) + "; " + str(self.arg1) + ")")
    # end-of-class(styp_let(styp))

print("styp_int2 = " + str(styp_int2))
print("styp_fun_int_int = " + str(styp_fun_int_int))

def styp_equal(st1, st2):
    if (st1.ctag == "STbas"):
        return st2.ctag == "STbas" and st1.arg1 == st2.arg1
    if (st1.ctag == "STtup"):
        return st2.ctag == "STtup" \
            and styp_equal(st1.arg1, st2.arg1) and styp_equal(st1.arg2, st2.arg2)
    if (st1.ctag == "STfun"):
        return st2.ctag == "STfun" \
            and styp_equal(st1.arg1, st2.arg1) and styp_equal(st1.arg2, st2.arg2)
    raise TypeError(st1) # HX-2025-06-10: should be deadcode!

##################################################################

# datatype term =
# | TMint of int
# | TMbtf of bool
# | TMvar of strn
# | TMlam of (strn, styp, term)
# | TMapp of (term, term)
# | TMopr of (strn(*opr*), list(term))
# | TMif0 of (term, term, term)
# | TMfix of (strn(*f*), strn(*x*), styp, styp, term)

class term:
    ctag = ""
    def __str__(self):
        return ("term(" + self.ctag + ")")
# end-of-class(term)

# | TMint of int
class term_int(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMint"
    def __str__(self):
        return ("TMint(" + str(self.arg1) + ")")
# end-of-class(term_int(term))

# | TMbtf of bool
class term_btf(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMbtf"
    def __str__(self):
        return ("TMbtf(" + str(self.arg1) + ")")
# end-of-class(term_btf(term))

# | TMvar of strn
class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMvar"
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")
# end-of-class(term_var(term))

# | TMlam of (strn(*var*), styp, term)
class term_lam(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMlam"
    def __str__(self):
        return ("TMlam(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(term_lam(term))

# | TMapp of (term, term)
class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + ";" + str(self.arg2) + ")")
# end-of-class(term_app(term))

# | TMopr of (strn(*opr*), list(term))
class term_opr(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMopr"
    def __str__(self):
        return ("TMopr(" + self.arg1 + ";" + str(self.arg2) + ")")
# end-of-class(term_opr(term))

# | TMif0 of (term, term, term)
class term_if0(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TMif0"
    def __str__(self):
        return ("TMif0(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(term_if0(term))

var_x = term_var("x")

term_add = lambda a1, a2: term_opr("+", [a1, a2])
term_sub = lambda a1, a2: term_opr("-", [a1, a2])
term_mul = lambda a1, a2: term_opr("*", [a1, a2])
term_div = lambda a1, a2: term_opr("/", [a1, a2])
term_mod = lambda a1, a2: term_opr("%", [a1, a2])

term_dbl = term_lam("x", styp_int, term_add(var_x, var_x))
print("term_dbl = " + str(term_dbl))

term_lt = lambda a1, a2: term_opr("<", [a1, a2])
term_lte = lambda a1, a2: term_opr("<=", [a1, a2])

# TMfix of
# (strn(*f*), strn(*x*), styp(*arg*), styp(*res*), term)
class term_fix(term):
    def __init__(self, arg1, arg2, arg3, arg4, arg5):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
        self.ctag = "TMfix"
    def __str__(self):
        return ("TMfix(" + self.arg1 + ";" + self.arg2 + ";" + str(self.arg3) + str(self.arg4) + ";" + str(self.arg5) + ")")
# end-of-class(term_fix(term))

##################################################################

# datatype tctx =
# | CXnil of ()
# | CXcons of (strn, styp, tctx)

class tctx:
    ctag = ""
    def __str__(self):
        return ("tctx(" + self.ctag + ")")
# end-of-class(tctx)

class tctx_nil(tctx):
    def __init__(self):
        self.ctag = "CXnil"
    def __str__(self):
        return ("CXnil(" + ")")
# end-of-class(tctx_nil(tctx))

class tctx_cons(tctx):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "CXcons"
    def __str__(self):
        return ("CXcons(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(tctx_cons(tctx))

##################################################################

# #extern
# fun
# term_tpck00(tm0: term): tval
# #extern
# fun
# term_tpck01(tm0: term, ctx: tctx): tval

def term_tpck00(tm0):
    return term_tpck01(tm0, tctx_nil())

def tctx_search(ctx, x00):
    if ctx.ctag == "CXnil":
        return None
    if ctx.ctag == "CXcons":
        if ctx.arg1 == x00:
            return ctx.arg2
        else:
            return tctx_search(ctx.arg3, x00)
    raise TypeError(ctx) # HX-2025-06-10: deadcode!

def term_tpck01(tm0, ctx):
    # print("term_tpck01: tm0 = " + str(tm0))
    if (tm0.ctag == "TMint"):
        return styp_bas("int")
    if (tm0.ctag == "TMbtf"):
        return styp_bas("bool")
    if (tm0.ctag == "TMvar"):
        st0 = tctx_search(ctx, tm0.arg1)
        assert st0 is not None
        return st0
    if (tm0.ctag == "TMlam"):
        x01 = tm0.arg1
        st1 = tm0.arg2
        tmx = tm0.arg3
        ctx = tctx_cons(x01, st1, ctx)
        stx = term_tpck01(tmx, ctx)
        return styp_fun(st1, stx)
    if (tm0.ctag == "TMapp"):
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        st1 = term_tpck01(tm1, ctx)
        st2 = term_tpck01(tm2, ctx)
        assert st1.ctag == "STfun"
        assert styp_equal(st1.arg1, st2)
        return st1.arg2
    if (tm0.ctag == "TMopr"):
        pnm = tm0.arg1
        ags = tm0.arg2 # list of arguments
        if (pnm == "+"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "-"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "*"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "-"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        if (pnm == "<"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == ">"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == "="):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == "<="):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == ">="):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == "!="):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_bool
        if (pnm == "cmp"):
            assert len(ags) == 2
            st1 = term_tpck01(ags[0], ctx)
            st2 = term_tpck01(ags[1], ctx)
            # print("TMopr: st1 = " + str(st1))
            # print("TMopr: st2 = " + str(st2))
            assert styp_equal(st1, styp_int)
            assert styp_equal(st2, styp_int)
            return styp_int
        raise TypeError(pnm) # HX-2025-06-10: unsupported!
    if (tm0.ctag == "TMif0"):
        tm1 = tm0.arg1
        st1 = term_tpck01(tm1, ctx)
        assert styp_equal(st1, styp_bool)
        st2 = term_tpck01(tm0.arg2, ctx) # then
        st3 = term_tpck01(tm0.arg3, ctx) # else
        assert styp_equal(st2, st3)
        return st2
    # TMfix of
    # (strn(*f*), strn(*x*), styp(*arg*), styp(*res*), term)
    if (tm0.ctag == "TMfix"):
        f00 = tm0.arg1
        x01 = tm0.arg2
        st1 = tm0.arg3 # type for x01
        st2 = tm0.arg4 # type for tmx
        tmx = tm0.arg5
        stf = styp_fun(st1, st2) # type for f00
        ctx = tctx_cons(f00, stf, ctx)
        ctx = tctx_cons(x01, st1, ctx)
        stx = term_tpck01(tmx, ctx)
        assert styp_equal(st2, stx)
        return stf
    
    # 6/24/25
    # TMtup of (term, term)
    if (tm0.ctag == "TMtup"):
        TMfst = term_tpck01(tm0.arg1, ctx)
        TMsnd = term_tpck01(tm0.arg2, ctx)
        return styp_tup(TMfst, TMsnd)
        
    if (tm0.ctag == "TMlet"):
        var_name = tm0.arg1
        bound_tm = tm0.arg2 
        body_tm  = tm0.arg3

        st_bound = term_tpck01(bound_tm, ctx)
        new_ctx = tctx_cons(var_name, st_bound, ctx)
        st_body = term_tpck01(body_tm, new_ctx)
        return styp_let(var_name, st_bound, st_body)


    raise TypeError(tm0) # HX-2025-06-10: should be deadcode!

int_0 = term_int(0)
int_1 = term_int(1)
int_2 = term_int(2)
btf_t = term_btf(True)
btf_f = term_btf(False)
print("tpck(int_1) = " + str(term_tpck00(int_1)))
print("tpck(btf_t) = " + str(term_tpck00(btf_t)))
print("tpck(term_add(int_1, int_1)) = " + str(term_tpck00(term_add(int_1, int_1))))
print("tpck(term_lte(int_1, int_1)) = " + str(term_tpck00(term_lte(int_1, int_1))))
# HX: this one is ill-typed:
# print("tpck(term_add(int_1, btf_t)) = " + str(term_tpck00(term_add(int_1, btf_t))))
print("tpck(term_dbl) = " + str(term_tpck00(term_dbl)))

int_0 = term_int( 0 )
int_1 = term_int( 1 )
var_f = term_var("f")
var_n = term_var("n")
int_3 = term_int(3)
int_5 = term_int(5)
int_10 = term_int(10)
term_fact = \
  term_fix("f", "n", styp_int, styp_int, \
    term_if0(term_lte(var_n, int_0), \
      int_1, \
      term_mul(var_n, term_app(var_f, term_sub(var_n, int_1)))))

print("tpck(term_fact) = " + str(term_tpck00(term_fact)))

##################################################################

CHNUM3 = \
  term_lam("f", styp_fun_int_int, \
    term_lam("x", styp_int, term_app(var_f, term_app(var_f, term_app(var_f, var_x)))))

print("tpck(CHNUM3) = " + str(term_tpck00(CHNUM3)))

##################################################################

# datatype treg =
# TREG of (strn(*prfx*), sint(*sffx*))

class treg:
    prfx = ""
    ntmp = 100
    nfun = 100
    def __init__(self, prfx, sffx):
        self.prfx = prfx; self.sffx = sffx
    def __str__(self):
        return ("treg(" + self.prfx + str(self.sffx) + ")")
# end-of-class(treg)

def targ_new():
    return treg("arg", 0)
def ttmp_new():
    treg.ntmp += 1
    return treg("tmp", treg.ntmp)
def tfun_new():
    treg.nfun += 1
    return treg("fun", treg.nfun)

arg0 = targ_new()
tmp1 = ttmp_new()
tmp2 = ttmp_new()
fun1 = tfun_new()
fun2 = tfun_new()
print("arg0 = " + str(arg0))
print("tmp1 = " + str(tmp1))
print("tmp2 = " + str(tmp2))
print("fun1 = " + str(fun1))
print("fun2 = " + str(fun2))

##################################################################

# datatype tval =
# | TVALint of sint
# | TVALbtf of bool
# | TVALchr of char
# | TVALstr of strn
# | TVALreg of treg

class tval:
    ctag = ""
    def __str__(self):
        return ("tval(" + self.ctag + ")")
# end-of-class(tval)

class tval_int(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVALint"
    def __str__(self):
        return ("TVALint(" + str(self.arg1) + ")")
# end-of-class(tval_int(tval))

class tval_btf(tval):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TVALbtf"
    def __str__(self):
        return ("TVALbtf(" + str(self.arg1) + ")")
# end-of-class(tval_btf(tval))

# datatype tins =
# | TINSmov of (treg(*dst*), tval(*src*))
# | TINSapp of (treg(*res*), treg(*fun*), treg(*arg*))
# | TINSopr of (treg(*res*), strn(*opr*), list(treg))
# | TINSfun of (treg(*f00*), tcmp(*body*))
# | TINSif0 of (treg(*res*), treg(*test*), tcmp(*then*), tcmp(*else*))

# datatype tcmp =
# | TCMP of (list(tins), treg(*res*))

class tins:
    ctag = ""
    def __str__(self):
        return ("tins(" + self.ctag + ")")
# end-of-class(tins)

class tins_mov(tins):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TINSmov"
    def __str__(self):
        return ("tins_mov(" + str(self.arg1) + ";" + str(self.arg2) + ")")

# | TINSopr of (treg(*res*), strn(*opr*), list(treg))
class tins_opr(tins):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TINSopr"
    def __str__(self):
        return ("tins_opr(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")

# | TINSapp of (treg(*res*), treg(*fun*), treg(*arg*))
class tins_app(tins):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TINSapp"
    def __str__(self):
        return ("tins_app(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")

# | TINSif0 of (treg(*res*), treg(*test*), tcmp(*then*), tcmp(*else*))
class tins_if0(tins):
    def __init__(self, arg1, arg2, arg3, arg4):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.ctag = "TINSif0"
    def __str__(self):
        return ("tins_if0(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ";" + str(self.arg4) + ")")

# | TINSfun of (treg(*f00*), tcmp(*body*), arg(*x*))
class tins_fun(tins):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "TINSfun"
    def __str__(self):
        return ("tins_fun(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")

# datatype tcmp =
# | TCMP of (list(tins), treg)


# tcmp(inss, reg) = inss -> reg
class tcmp:
    def __init__(self, inss, treg):
        self.arg1 = inss; self.arg2 = treg
    def __str__(self):
        return ("tcmp(" + "..." + ";" + str(self.arg2) + ")")
# end-of-class(tcmp)

##################################################################

# datatype cenv =
# | CENVnil of ()
# | CENVcons of (strn, treg, cenv)

class cenv:
    ctag = ""
    def __str__(self):
        return ("cenv(" + self.ctag + ")")
# end-of-class(cenv)

class cenv_nil(cenv):
    def __init__(self):
        self.ctag = "CENVnil"
    def __str__(self):
        return ("CENVnil(" + ")")
# end-of-class(cenv_nil(cenv))

class cenv_cons(cenv):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "CENVcons"
    def __str__(self):
        return ("CENVcons(" + self.arg1 + ";" + str(self.arg2) + ";" + str(self.arg3) + ")")
# end-of-class(cenv_cons(cenv))

##################################################################

def term_comp00(tm0): # "computation"
    return term_comp01(tm0, cenv_nil())

def cenv_search(env, x00):
    if env.ctag == "CENVnil":
        return None
    if env.ctag == "CENVcons":
        if env.arg1 == x00:
            return env.arg2
        else:
            return cenv_search(env.arg3, x00)
    raise TypeError(env) # HX-2025-06-10: deadcode!

def term_comp01(tm0, cenv):
    if (tm0.ctag == "TMint"):
        ttmp = ttmp_new()
        ins0 = tins_mov(ttmp, tval_int(tm0.arg1))
        return tcmp([ins0], ttmp)
    if (tm0.ctag == "TMbtf"):
        ttmp = ttmp_new()
        ins0 = tins_mov(ttmp, tval_btf(tm0.arg1))
        return tcmp([ins0], ttmp)
    if (tm0.ctag == "TMvar"):
        x01 = tm0.arg1
        tmp1 = cenv_search(cenv, x01)
        return tcmp([], tmp1)
    if (tm0.ctag == "TMopr"):
        pnm = tm0.arg1
        ags = tm0.arg2 # list of arguments
        if (pnm == "+"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "+", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "-"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "-", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "*"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "*", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "/"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "/", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "%"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "%", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == ">"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, ">", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "<"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "<", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == ">="):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, ">=", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "<="):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "<=", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "="):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "=", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "!="):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "!=", [tmp1, tmp2])]
            return tcmp(inss, ttmp)
        if (pnm == "cmp"):
            assert len(ags) == 2
            cmp1 = term_comp01(ags[0], cenv)
            cmp2 = term_comp01(ags[1], cenv)
            ins1 = cmp1.arg1
            tmp1 = cmp1.arg2
            ins2 = cmp2.arg1
            tmp2 = cmp2.arg2
            ttmp = ttmp_new()
            inss = ins1 + ins2 + [tins_opr(ttmp, "cmp", [tmp1, tmp2])]
            return tcmp(inss, ttmp)

        raise TypeError(pnm) # HX-2025-06-18: unsupported!
    if (tm0.ctag == "TMapp"):    
        cmp1 = term_comp01(tm0.arg1, cenv)
        cmp2 = term_comp01(tm0.arg2, cenv)
        ins1 = cmp1.arg1
        tmp1 = cmp1.arg2
        ins2 = cmp2.arg1
        tmp2 = cmp2.arg2
        ttmp = ttmp_new()
        inss = ins1 + ins2 + [tins_app(ttmp, tmp1, tmp2)]
        return tcmp(inss, ttmp)
    if (tm0.ctag == "TMlam"):
        x01 = tm0.arg1
        fun0 = tfun_new()
        arg0 = targ_new()
        cenv = cenv_cons(x01, arg0, cenv)
        cmp1 = term_comp01(tm0.arg3, cenv)
        inss = [tins_fun(fun0, cmp1, arg0)]
        return tcmp(inss, fun0)
    if (tm0.ctag == "TMif0"):
        cmp1 = term_comp01(tm0.arg1, cenv) # test
        cmp2 = term_comp01(tm0.arg2, cenv) # then
        cmp3 = term_comp01(tm0.arg3, cenv) # else
        ins1 = cmp1.arg1
        tmp1 = cmp1.arg2
        ttmp = ttmp_new()
        ins0 = tins_if0(ttmp, tmp1, cmp2, cmp3)
        inss = ins1 + [ins0]
        return tcmp(inss, ttmp)
    if (tm0.ctag == "TMfix"):
        f00 = tm0.arg1
        x01 = tm0.arg2
        fun0 = tfun_new()
        arg0 = targ_new()
        cenv = cenv_cons(f00, fun0, cenv)
        cenv = cenv_cons(x01, arg0, cenv)
        cmp1 = term_comp01(tm0.arg5, cenv)
        inss = [tins_fun(fun0, cmp1, arg0)]
        return tcmp(inss, fun0)
        
    ##################################################################
    #           Task 1
    ##################################################################

    # tup
    # first projection 
    # second projection 
    # let 
    # remain opr things
 

    ##################################################################
    
    


    # TMtup
    if tm0.ctag == "TMtup":
        cmp1 = term_comp01(tm0.arg1, cenv)  # compile fst 
        cmp2 = term_comp01(tm0.arg2, cenv)  #     and snd
        inss = cmp1.arg1
        r1 = cmp1.arg2
        inss2 = cmp2.arg1
        r2 =  cmp2.arg2
        ttmp = ttmp_new()      # allocate result
        return tcmp(inss + inss2 + [tins_opr(ttmp, "tup", [r1, r2])], ttmp)

    # TMfst 
    if tm0.ctag == "TMfst":
        cmp1 = term_comp01(tm0.arg1, cenv)
        inss = cmp1.arg1
        rtup = cmp1.arg2
        ttmp = ttmp_new()
        return tcmp(inss + [tins_opr(ttmp, "fst", [rtup])], ttmp)

    # TMsnd 
    if tm0.ctag == "TMsnd":
        cmp1 = term_comp01(tm0.arg1, cenv)
        inss = cmp1.arg1
        rtup = cmp1.arg2
        ttmp = ttmp_new()
        return tcmp(inss + [tins_opr(ttmp, "snd", [rtup])], ttmp)

    # TMlet
    if tm0.ctag == "TMlet":
        # let x = bound_tm in body_tm
        x01 = tm0.arg1
        bond = tm0.arg2
        body = tm0.arg3

        # compile the binding, stick its result into x’s register
        cmp1 = term_comp01(bond, cenv)
        inss = cmp1.arg1
        arg0 = cmp1.arg2

        # extend the compilation environment so that occurrences of x
        # map to rbound
        new_env = cenv_cons(x01, arg0, cenv)

        # compile the body under that mapping
        cmp2 = term_comp01(body, new_env)
        inss_body = cmp2.arg1
        rbody = cmp2.arg2

        # overall instrs flow: first do the binding then the body
        return tcmp(inss + inss_body, rbody)


    raise TypeError(tm0) # HX-2025-06-18: unsupported!

print("comp00(int_1) = " + str(term_comp00(int_1)))
print("comp00(btf_t) = " + str(term_comp00(btf_t)))
print("comp00(term_add(int_1, int_2)) = " + str(term_comp00(term_add(int_1, int_2))))
print("comp00(term_dbl) = " + str(term_comp00(term_dbl)))
# print("comp00(term_fact) = " + str(term_comp00(term_fact)))

##################################################################

# datatype tins =
# | TINSmov of (treg(*dst*), tval(*src*))
# | TINSapp of (treg(*res*), treg(*fun*), treg(*arg*))
# | TINSopr of (treg(*res*), strn(*opr*), list(treg))
# | TINSfun of (treg(*f00*), tcmp(*body*), arg(*x*))
# | TINSif0 of (treg(*res*), treg(*test*), tcmp(*then*), tcmp(*else*))

def strn_emit(strn):
    print(strn, end='')

def endl_emit(strn):
    strn_emit('\n')

# value emits
def tval_emit(tval):
    strn_emit(str(tval))

# register emits
def treg_emit(treg):
    strn_emit(str(treg))


# num of indents
def nind_emit(nind):
    i0 = 0
    while(i0 < nind):
        i0 = i0 + 1
        strn_emit(' ')
    return None

def args_emit(args):
    i0 = 0
    n0 = len(args)
    while(i0 < n0):
        if (i0 >= 1):
            strn_emit(', ')
        treg_emit(args[i0])
        i0 = i0 + 1
    return None

#def emit(ins):

"""
def tins_emit(nind, tins):
    nind_emit(nind)
    if (tins.ctag == "TINSmov"):
        treg_emit(tins.arg1); strn_emit(' = '); tval_emit(tins.arg2); endl_emit()
    if (tins.ctag == "TINSapp"):
        treg_emit(tins.arg1); strn_emit(' = '); \
        treg_emit(tins.arg2); strn_emit('('); treg_emit(tins.arg3); strn_emit(')'); endl_emit()
    if (tins.ctag == "TINSopr"):
        treg_emit(tins.arg1); strn_emit(' = '); \
        strn_emit(tins.arg2); strn_emit('('); args_emit(tins.arg3); strn_emit(')'); endl_emit()
    # HX: please finish the rest of the cases
    if (tins.ctag == "TINSfun"):
        treg_emit(tins.arg1); strn_emit(' = '); endl_emit()
    if (tins.ctag == "TINSif0"):
        treg_emit(tins.arg1); strn_emit(' = '); treg_emit(tins.arg2); 
        

    raise TypeError(tins) # HX-2025-06-24: should be deadcode!  
"""
#helpers for functions
def name(r):
        return f"{r.prfx}{r.sffx}" # represents tmp101 or fun101
indent = "    "

#################################################
#                   Task 2
#################################################

def tcmp_pyemit(cmp_inst):
    ins_list = cmp_inst.arg1
    if not ins_list:
        return
    
    first = ins_list[0]
    if first.ctag == "TINSfun":
        fun_reg, arg_reg, body = first.arg1, first.arg3, first.arg2

        # header: def fun(arg0):
        print(f"def {name(fun_reg)}({name(arg_reg)}):")

        # body: start the recursive call to emit the rest of the body
        for ins in body.arg1:
            tins_emit(ins, 1)

        # return
        print(f"{indent}return {name(body.arg2)}")

    # CASE B: a flat script
    else:
        for ins in ins_list:
            tins_emit(ins, 0)
        # after you've emitted all the statements, print the result
        print(f"print({name(cmp_inst.arg2)})")

def tins_emit(ins, depth):
    """ emits instruction from ins"""
    i = indent * depth

    # | TINSmov of (treg(*dst*), tval(*src*))
    if ins.ctag == "TINSmov":
        dst, val = name(ins.arg1), ins.arg2.arg1
        print(f"{i}{dst} = {val}")

    # | TINSapp of (treg(*res*), treg(*fun*), treg(*arg*))
    elif ins.ctag == "TINSapp":
        dst, f, a = name(ins.arg1), name(ins.arg2), name(ins.arg3)
        print(f"{i}{dst} = {f}({a})")

    # | TINSopr of (treg(*res*), strn(*opr*), list(treg))
    elif ins.ctag == "TINSopr":
        dst = name(ins.arg1)
        pnm = ins.arg2
        (a, b) = ins.arg3
        print(f"{i}{dst} = {name(a)} {pnm} {name(b)}")

    # | TINSfun of (treg(*f00*), tcmp(*body*), arg(*x*))
    elif ins.ctag == "TINSfun":
        endl_emit("")
        # pretty much the same from emit()
        fun_reg = ins.arg1
        arg_reg = ins.arg3
        body = ins.arg2

        # header: def fun(arg0):
        print(f"{i}def {name(fun_reg)}({name(arg_reg)}):")

        # body: start the recursive call to emit the rest of the body
        for ins in body.arg1:
            tins_emit(ins, depth+1)

        # return
        print(f"{i + indent}return {name(body.arg2)}")
        endl_emit("")

    # | TINSif0 of (treg(*res*), treg(*test*), tcmp(*then*), tcmp(*else*))
    elif ins.ctag == "TINSif0":
        endl_emit("")
        res = name(ins.arg1)
        test = name(ins.arg2) # test
        then_cmp = ins.arg3 # then
        else_cmp = ins.arg4 # else

        print(f"{i}if {test}:")
        for ins in then_cmp.arg1:
            tins_emit(ins, depth+1)
        
        print(f"{i}{indent}{res} = {name(then_cmp.arg2)}")

        print(f"{i}else:")
        for ins in else_cmp.arg1:
            tins_emit(ins, depth+1)
        
        print(f"{i}{indent}{res} = {name(else_cmp.arg2)}")
        endl_emit("")
    else:
        raise TypeError(f"unhandled emit for {ins.ctag}")

# datatype tins =
# | TINSmov of (treg(*dst*), tval(*src*))
# | TINSapp of (treg(*res*), treg(*fun*), treg(*arg*))
# | TINSopr of (treg(*res*), strn(*opr*), list(treg))
# | TINSfun of (treg(*f00*), tcmp(*body*), arg(*x*))
# | TINSif0 of (treg(*res*), treg(*test*), tcmp(*then*), tcmp(*else*)) 

##################################################################
# end of [CS391-2025-Summer/lectures/lecture-06-24/lambda3.py]
##################################################################
print("\n" * 2)
print("factorial function \n")
tcmp_pyemit(term_comp00(term_fact))


int_2        = term_int(2)
var_i        = term_var("i")
var_checkDiv = term_var("checkDiv")

term_isPrime = \
  term_fix("isPrime", "n", styp_int, styp_int, \
    term_if0(term_lte(var_n, int_1), \
      int_0, \
      term_app( \
        term_fix("checkDiv", "i", styp_int, styp_int, \
          term_if0(term_lte(var_i, term_sub(var_n, int_1)), \
            term_if0(term_mod(var_n, var_i), \
              term_app(var_checkDiv, term_add(var_i, int_1)), \
              int_0), \
            int_1) \
        ), \
        int_2 \
      ) \
    ) \
  )

print("\n" * 2)
print("isPrime function \n")
tcmp_pyemit(term_comp00(term_isPrime))


term_fib = \
        term_fix("f","n", styp_int, styp_int,
              term_if0(
                term_lte(var_n, term_int(1)),
                var_n,
                term_add(
                  term_app(var_f, term_sub(var_n, term_int(1))),
                  term_app(var_f, term_sub(var_n, term_int(2)))
                )
            )
        )



print("\n" * 2)
print("Fibonacci Sequence \n")
tcmp_pyemit(term_comp00(term_fib))