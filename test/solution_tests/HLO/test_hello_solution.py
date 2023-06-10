from solutions.HLO import hello_solution


class TestHLO:
    def test_hello(self):
        # ARRANGE
        expected_result = "Hello, World!"
        # ACT
        result = hello_solution.hello("some string")
        # ASSERT
        assert result == expected_result

