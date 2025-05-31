

class term:
    ctag = ""
    def __str__(self):
        return ("term(" + self.ctag + ")")

class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = "TMvar"
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")

class term_lam(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMlam"
    def __str__(self):
        return ("TMlam(" + self.arg1 + "," + str(self.arg2) + ")")
    
class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + "," + str(self.arg2) + ")")


class term_int(term):
    def __init__(self, sint):
        self.sint = sint
        self.ctag = "TMint"
    def __str__(self):
        return ("TMopr(" + str(self.sint) + ")")

class term_bool(term):
    def __init__(self, bool):
        self.bool = bool
        self.ctag = "TMbtf"
    def __str__(self):
        return ("TMbtf(" + str(self.bool) + ")")


class term_opr(term):
    def __init__(self, operator, termList):
        self.topr = operator
        self.tlst = termList
        self.ctag = "TMopr"
    def __str__(self):
        return ("TMopr(" + str(self.topr) + ", " + str(self.tlst) + ")")
    

class term_if0(term):
    def __init__(self, condition, true, false):
        self.cond = condition
        self.ctru = true
        self.cfls = false
        self.ctag = "TMif0"
    def __str__(self):
        return ("TMif0(" + str(self.cond) + ", " + str(self.ctru) + ", " + str(self.cfls) + ")")



#Start Question 1
fix = term_lam("f",
        term_app( 
            term_lam("x",
                term_app(
                    term_var("f"),
                    term_app(term_var("x"), term_var("x"))
                )
            ),
            term_lam("x",
                term_app(
                    term_var("f"),
                    term_app(term_var("x"), term_var("x"))
                )
            )
        )
    )

fib = term_app(
        fix,
        (term_lam("fibo",
                term_lam("n",
                    term_if0(
                        term_opr("<=", [term_var("n"), term_int(1)]),
                        term_var("n"),
                        term_opr("+", [
                                    term_app( term_var("fibo"), term_opr ("-", [term_var("n"), term_int(1)])),
                                    term_app( term_var("fibo"), term_opr ("-", [term_var("n"), term_int(2)]))
                                    
                        ])
                    )
                )   
            )
        )
    )
#End Question

#Start Question 2

#My implementation
def isPrime(n):
    def help(num, num2):
        if num2 <= 1:
            return True
        if num % num2 == 0:
            return False
        return help(num, num-1)
    
    return help(n, n)

#Lambda Calc translation

fix = term_lam("f",
        term_app( 
            term_lam("x",
                term_app(
                    term_var("f"),
                    term_app(term_var("x"), term_var("x"))
                )
            ),
            term_lam("x",
                term_app(
                    term_var("f"),
                    term_app(term_var("x"), term_var("x"))
                )
            )
        )
    )


isPrime = term_lam("num",
                term_app(
                    fix,
                    term_lam("isPrime",
                            term_lam("num", 
                                    term_lam("help",
                                            term_if0(
                                                term_opr("<=", [term_var("num2"), term_int(1)]),
                                                term_bool("TRUE"),
                                                term_if0(
                                                    term_opr("==", [term_opr("%", [term_var("num"), term_var("num2")]), term_int(0)]),
                                                    term_bool("FALSE"),
                                                    term_app(
                                                        (term_app(term_var("help"), term_var("num")) ),
                                                        term_var("num")       
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )

#End Question 2


#Question 3

# datatype term =
# | TMvar of strn
# | TMlam of (strn, term)
# | TMapp of (term, term)

class term:
    ctag = ""
    def __str__(self):
        return ("term(" + self.ctag + ")")
# end-of-class(term)

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
        return ("TMlam(" + self.arg1 + "," + str(self.arg2) + ")")
# end-of-class(term_lam(term))

class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = "TMapp"
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(term_app(term))

class term_int(term):
        def __init__(self, sint):
            self.sint = sint
            self.ctag = "TMint"
        def __str__(self):
            return ("TMopr(" + str(self.sint) + ")")

class term_bool(term):
        def __init__(self, bool):
            self.bool = bool
            self.ctag = "TMbtf"
        def __str__(self):
            return ("TMbtf(" + str(self.bool) + ")")


class term_opr(term):
        def __init__(self, operator, termList):
            self.topr = operator
            self.tlst = termList
            self.ctag = "TMopr"
        def __str__(self):
            return ("TMopr(" + str(self.topr) + ", " + str(self.tlst) + ")")
        

class term_if0(term):
        def __init__(self, condition, true, false):
            self.cond = condition
            self.ctru = true
            self.cfls = false
            self.ctag = "TMif0"
        def __str__(self):
            return ("TMif0(" + str(self.cond) + ", " + str(self.ctru) + ", " + str(self.cfls) + ")")
        

def term_subst(tm0, x00, sub):
    def subst(tm0):
        if type(tm0.termList) == list:
            return [term_subst(tm0.termList[0], x00, sub), term_subst(tm0.termList[1], x00, sub)]
        
        return term_subst(tm0, x00, sub)
    # |TMvar(x1) =>
    #  if x0 = x1 then u0 else t0
    if (tm0.ctag == "TMvar"):
        x01 = tm0.arg1
        # print("term_subst: TMvar")
        # print("x00 = " + x00)
        # print("x01 = " + x01)
        return sub if (x00==x01) else tm0
    # |TMlam(x1, t1) =>
    #  if x0 = x1
    #  then t0 else TMlam(x1, term_subst(t1, x0, u0))
    if (tm0.ctag == "TMlam"):
        x01 = tm0.arg1
        tm1 = tm0.arg2
        return tm0 if (x00==x01) else term_lam(x01, subst(tm1))
    # |TMapp(t1, t2) =>
    #  TMapp(term_subst(t1, x0, u0), term_subst(t2, x0, u0))
    if (tm0.ctag == "TMapp"):
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        return term_app(subst(tm1), subst(tm2))
    if tm0.ctag == "TMint":
        return tm0
    if tm0.ctag == "TMbtf":
        return tm0
    if tm0.ctag == "TMif0":
        return term_if0(subst(tm0.condition), subst(tm0.true), subst(tm0.false))
    if tm0.ctag == "TMopr":
        return term_opr(subst(tm0.operator), subst(tm0.termList))


    raise TypeError(tm0) # HX-2025-05-27: should be deadcode!

