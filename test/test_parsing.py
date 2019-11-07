import unittest
from parsing import (
    tokenize,
    read_from_tokens,
    atom
)


class TestParsing(unittest.TestCase):

    def setUp(self):
        expression = '(abc)'
        self.expression_tokenized = tokenize(expression)

    def test_tokenize_should_split_string(self):
        assert self.expression_tokenized == ['(', 'abc', ')']

    def test_read_from_tokens_must_return_error(self):
        expression_empty = []
        with self.assertRaises(SyntaxError):
            read_from_tokens(expression_empty)


class TestAtom(unittest.TestCase):

    def test_atom_should_return_float(self):
        float_number = 9.5
        assert atom('9.5') == float_number

    def test_atom_should_return_int(self):
        int_number = 42
        assert atom('42') == int_number

    def test_atom_should_return_symbol(self):
        symbol_number = '*'
        assert atom('*') == symbol_number












if __name__ == "__main__":
    unittest.main()