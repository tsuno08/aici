"""
シンプルな計算機モジュール
"""


class Calculator:
    """基本的な算術演算を提供する計算機クラス"""

    def add(self, a, b):
        """2つの数値を加算する

        Args:
            a: 1つ目の数値
            b: 2つ目の数値

        Returns:
            a + b の結果
        """
        return a + b

    def subtract(self, a, b):
        """2つの数値を減算する

        Args:
            a: 1つ目の数値
            b: 2つ目の数値

        Returns:
            a - b の結果
        """
        return a - b

    def multiply(self, a, b):
        """2つの数値を乗算する

        Args:
            a: 1つ目の数値
            b: 2つ目の数値

        Returns:
            a * b の結果
        """
        return a * b

    def divide(self, a, b):
        """2つの数値を除算する

        Args:
            a: 1つ目の数値
            b: 2つ目の数値

        Returns:
            a / b の結果

        Raises:
            ZeroDivisionError: bが0の場合
        """
        if b == 0:
            raise ZeroDivisionError("0で割ることはできません")
        return a / b