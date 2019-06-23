"""Procedures"""

from environment import (
    GLOBAL_ENV,
    Env,
    Symbol,
    List
)


class Procedure:
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env

    def __call__(self, *args):
        return eval_lisp(self.body, Env(self.parms, args, self.env))

def eval_lisp(exp_lisp, env=GLOBAL_ENV):
    "Evaluate an expression in an environment."
    if isinstance(exp_lisp, Symbol):        # variable reference
        return env.find(exp_lisp)[exp_lisp]
    elif not isinstance(exp_lisp, List):    # constant literal
        return exp_lisp
    elif exp_lisp[0] == 'if':               # conditional
        (_, test, conseq, alt) = exp_lisp
        exp = (conseq if eval_lisp(test, env) else alt)
        return eval_lisp(exp, env)
    elif exp_lisp[0] == 'define':         # (define var exp)
        (_, var, exp) = exp_lisp
        env[var] = eval_lisp(exp, env)
    elif exp_lisp[0] == 'set!':           # (set! var exp)
        (_, var, exp) = exp_lisp
        env.find(var)[var] = eval_lisp(exp, env)
    elif exp_lisp[0] == 'lambda':         # (lambda (var...) body)
        (_, parms, body) = exp_lisp
        return Procedure(parms, body, env)
    else:
        proc = eval_lisp(exp_lisp[0], env)
        args = [eval_lisp(exp, env) for exp in exp_lisp[1:]]
        return proc(*args)
