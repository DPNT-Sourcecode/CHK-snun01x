from solutions.HLO import hello_solution


class TestHLO:
    def test_hello(self, hello_world):
        # ARRANGE
        # ACT
        result = hello_solution.hello("some string")
        # ASSERT
        assert result == hello_world



