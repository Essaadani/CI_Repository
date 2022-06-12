import calculator

class TestCalc:
    def test_sum(self):
        assert 8 == calculator.sum(4, 4)