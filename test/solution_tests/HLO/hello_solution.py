import pytest
from solutions.HLO import hello_solution


class TestHLO:
    def test_hello(self):
        hello_solution.hello('string')


