import sys
sys.setrecursionlimit(10000)

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

# HX-2025-06-10:
# for handling tuples of length 2:
# | TMfst of term // first projection
# | TMsnd of term // second projection
# | TMtup of (term, term) // tuple construction
# 
# for (let x = t1 in t2), which stands for (lam x. t1)(t2):
# | TMlet of (strn(*x*), term(*t1*), term(*t2))

class term:
    ctag = ""
    def __str__(self):
        return "term(" + self.ctag + ")"

# | TMint of int
class term_int(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMint"
    def __str__(self):
        return "TMint(" + str(self.arg1) + ")"

# | TMbtf of bool
class term_btf(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMbtf"
    def __str__(self): 
        return "TMbtf(" + str(self.arg1) + ")"

# | TMvar of strn
class term_var(term):
    def __init__(self, arg1): 
        self.arg1 = arg1 
        self.ctag = "TMvar"
    def __str__(self): 
        return "TMvar(" + self.arg1 + ")"

# | TMlam of (strn(*var*), styp, term)
class term_lam(term):
    def __init__(self, arg1, body): 
        self.arg1 = arg1
        self.body = body
        self.ctag = "TMlam"
    def __str__(self):
        return "TMlam(" + self.arg1 + ";" + str(self.body) + ")"

# | TMapp of (term, term)
class term_app(term):
    def __init__(self, arg1, arg2): 
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self): 
        return "TMapp(" + str(self.arg1) + ";" + str(self.arg2) + ")"

# | TMopr of (strn(*opr*), list(term))
class term_opr(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMopr"
    def __str__(self):
        return "TMopr(" + self.arg1 + ";" + str(self.arg2) + ")"

# | TMif0 of (term, term, term)
class term_if0(term):
    def __init__(self, c,t,e): 
        self.arg1 = c
        self.arg2 = t
        self.arg3 = e
        self.ctag = "TMif0"
    def __str__(self):
        return "TMif0(" + str(self.arg1) + ";" + str(self.arg2) + ";" + str(self.arg3) + ")"

class term_fix(term):
    def __init__(self, f,x,body): 
        self.arg1 = f
        self.arg2 = x
        self.arg3 = body
        self.ctag = "TMfix"
    def __str__(self): 
        return "TMfix(" + self.arg1 + ";" + self.arg2 + ";" + str(self.arg3) + ")"

class term_tup(term):
    def __init__(self, a,b): 
        self.arg1=a
        self.arg2=b
        self.ctag="TMtup"
    def __str__(self): 
        return "TMtup("+str(self.arg1)+";"+str(self.arg2)+")"

class term_fst(term):
    def __init__(self,a):
        self.arg=a
        self.ctag="TMfst"
    def __str__(self):
        return "TMfst("+str(self.arg)+")"

class term_snd(term):
    def __init__(self,a):
        self.arg=a; self.ctag="TMsnd"
    def __str__(self):
        return "TMsnd("+str(self.arg)+")"

class term_let(term):
    def __init__(self,v,val,body): 
        self.var=v
        self.val=val
        self.body=body
        self.ctag="TMlet"
    def __str__(self):
        return "TMlet(" + self.var + ";" + str(self.val) + ";" + str(self.body) + ")"

class term_unit(term):
    def __init__(self):
        self.ctag="TMunit"
    def __str__(self): 
        return "TMunit"
    
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

print("styp_int2 = " + str(styp_int2))
print("styp_fun_int_int = " + str(styp_fun_int_int))

class styp_let:
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = "STlet"
    def __str__(self):
        return ("STlet(" + str(self.arg1) + "; " + str(self.arg2) + "; " + str(self.arg1) + ")")
    # end-of-class(styp_let(styp))

       

def styp_equal(st1, st2):
    if (st1.ctag == "STbas"):
        return st2.ctag == "STbas" and st1.arg1 == st2.arg1
    if (st1.ctag == "STtup"):
        return st2.ctag == "STtup" \
            and styp_equal(st1.arg1, st2.arg1) and styp_equal(st1.arg2, st2.arg2)
    if (st1.ctag == "STfun"):
        return st2.ctag == "STfun" \
            and styp_equal(st1.arg1, st2.arg1) and styp_equal(st1.arg2, st2.arg2)
    if (st1.ctag == "STlet"):
        return styp_equal(st1.arg1, st2.arg1) and styp_equal(st1.arg2, st2.arg2) and styp_equal(st1.arg3, st2.arg3)
    
    raise TypeError(st1) # HX-2025-06-10: should be deadcode!

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

class tval_tup(tval):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TVtup"
    def __str__(self):
        return ("TVtup(" + str(self.arg1) + ";" + str(self.arg2) + ")")


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
# term_eval01(tm0: term, env: xenv): tval

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
        
    if tm0.ctag == "TMlet":
        x01, tm1, tm2 = tm0.arg1, tm0.arg2, tm0.arg3
        bound_tv = term_eval01(tm1, env)
        new_env  = xenv_cons(x01, bound_tv, env)
        return term_eval01(tm2, new_env)
    if tm0.ctag == "TMtup":
        v1 = term_eval01(tm0.arg1, env)
        v2 = term_eval01(tm0.arg2, env)
        return tval_tup((v1, v2))

    if tm0.ctag == "TMfst":
        tup = term_eval01(tm0.arg1, env)
        assert tup.ctag == "TVtup"
        return tup.arg1[0]

    if tm0.ctag == "TMsnd":
        tup = term_eval01(tm0.arg1, env)
        assert tup.ctag == "TVtup"
        return tup.arg1[1]
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


# Board size
N = 8

# Print basics
def printRow(col): 
    return term_opr("printRow", [col])

def printBoard(bd):
    return term_opr("printBoard", [bd])

def incSol(n): 
    return term_opr("incSol", [n])

########################################################

# --- board_get: get((bd,i)) ---
board_get = term_fix("get","arg",
    term_lam("arg",
      term_if0(
        term_opr("=", [term_snd(term_var("arg")), term_int(0)]),
        term_fst(term_var("arg")),
        term_app(
          term_app(term_var("get"), 
            term_tup(
              term_snd(term_fst(term_var("arg"))),
              term_opr("-", [term_snd(term_var("arg")), term_int(1)])
            )
          ), term_unit()
        )
      )
    )
)

# --- Simplified recursive board_set: set((bd,i),j) ---
board_set = term_fix("set","arg",
    term_lam("arg",
      term_if0(
        term_opr("=", [term_snd(term_var("arg")), term_int(0)]),
        term_tup(
          term_var("j"),
          term_snd(term_fst(term_var("arg")))
        ),
        term_tup(
          term_fst(term_fst(term_var("arg"))),
          term_app(
            term_app(term_var("set"),
              term_tup(
                term_snd(term_fst(term_var("arg"))),
                term_opr("-", [term_snd(term_var("arg")), term_int(1)])
              )
            ), term_unit()
          )
        )
      )
    )
)

# safety_test1 unchanged
safety_test1 = term_lam("i0",
  term_lam("j0",
  term_lam("i",
  term_lam("j",
    term_opr("and", [
      term_opr("<>", [term_var("j0"), term_var("j")]),
      term_opr("<>", [
        term_opr("abs", [term_opr("-", [term_var("i0"), term_var("i")])]),
        term_opr("abs", [term_opr("-", [term_var("j0"), term_var("j")])])
      ])
    ])
  ))))

# --- safety_test2 ---
safety_test2 = term_fix("safe2","arg",
    term_lam("arg",
      term_if0(
        term_opr("<", [term_snd(term_var("arg")), term_int(0)]),
        term_btf(True),
        term_if0(
          term_app(
            term_app(
              term_app(
                term_app(term_var("safety_test1"), term_fst(term_var("arg"))),
                term_snd(term_var("arg"))),
              term_snd(term_var("arg"))
            ),
            term_app(term_var("safe2"),
              term_tup(
                term_fst(term_var("arg")),
                term_opr("-", [term_snd(term_var("arg")), term_int(1)])
              )
            ),
            term_btf(False)
        )
      )
    )
))

# search
search = term_fix("search", "arg",
  term_lam("arg",
    term_let("bd",
      term_fst(term_var("arg")),
      term_let("coords",
        term_snd(term_var("arg")),
        term_let("i",
          term_fst(term_var("coords")),
          term_let("j",
            term_snd(term_var("coords")),
            term_let("n",
              term_app(term_snd, term_var("arg")),
              term_if0(
                term_opr("<", [term_var("j"), term_int(N)]),
                # then‐branch
                term_if0(
                  term_app(
                    term_app(
                      term_app(
                        term_app(term_var("safety_test2"),
                                term_tup(term_var("i"), term_var("j"))),
                        term_var("bd")),
                      term_var("i")
                    ),
                    term_unit()
                  ),
                  term_let("bd1",
                    term_app(
                      term_app(term_var("board_set"), term_var("bd")),
                      term_var("j")
                    ),
                    term_if0(
                      term_opr("=", [
                        term_opr("+", [term_var("i"), term_int(1)]),
                        term_int(N)
                      ]),
                      printBoard(term_var("bd1")),
                      term_app(
                        term_app(term_var("search"),
                          term_tup(term_var("bd1"),
                            term_tup(
                              term_opr("+", [term_var("i"), term_int(1)]),
                              term_var("n")
                            )
                          )
                        ),
                        term_unit()
                      )
                    )
                  )
                ),
                # else-branch
                term_app(
                  term_app(term_var("search"),
                    term_tup(
                      term_var("bd"),
                      term_tup(term_var("i"),
                               term_opr("+", [term_var("j"), term_int(1)]))
                    )
                  ),
                  term_unit()
                )
              ),
              # final else for the outer term_if0
              term_if0(
                term_opr(">", [term_var("i"), term_int(0)]),
                term_app(
                  term_app(term_var("search"),
                    term_tup(term_var("bd"), term_var("n"))
                  ),
                  term_unit()
                ),
                term_var("n")
              )
            )
          )
        )
      )
    )
  )
)

# initial board
def make_initial(n):
    if n < 0:
        return term_unit()
    return term_tup(term_int(n), make_initial(n-1))
initial_bd = make_initial(7)

# main entry
main0 = term_app(term_app(term_var("search"), 
                          term_tup(initial_bd, 
                                   term_tup(term_int(0), 
                                   term_int(0)))),
                          term_unit())