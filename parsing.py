"""Parsing - parse, tokenize and read_from_tokens"""

from environment import Symbol

def parse(program):
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def tokenize(char):
    "Convert a string of characters into a list of tokens."
    return char.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from_tokens(tokens):
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        exp_list = []
        while tokens[0] != ')':
            exp_list.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return exp_list
    if token == ')':
        raise SyntaxError('unexpected )')
    return atom(token)

def atom(token):
    "Numbers become numbers; every other token is a symbol."
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)
