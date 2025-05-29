"""
計算機モジュールのテスト
"""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Calculatorクラスのテスト"""

    def setup_method(self):
        """各テストメソッドの前に実行される"""
        self.calc = Calculator()

    def test_add(self):
        """add メソッドのテスト"""
        assert self.calc.add(1, 2) == 3
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(-1, -1) == -2

    def test_subtract(self):
        """subtract メソッドのテスト"""
        assert self.calc.subtract(3, 2) == 1
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(-1, -1) == 0

    def test_multiply(self):
        """multiply メソッドのテスト"""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(-2, -3) == 6

    def test_divide(self):
        """divide メソッドのテスト"""
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(6, -3) == -2
        assert self.calc.divide(-6, -3) == 2

    def test_divide_by_zero(self):
        """0による除算のテスト"""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(6, 0)