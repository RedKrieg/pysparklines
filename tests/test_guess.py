import pytest
import sparkline


def test_convert():
    assert sparkline.sparkline._convert_to_float("1.0") == 1.0
    assert sparkline.sparkline._convert_to_float("Garbage") == None


def test_int():
    assert sparkline.guess_series("Garbage 1 2 3") == [1.0, 2.0, 3.0]


def test_exponent():
    assert sparkline.guess_series("-1.1e-4 5.5 2.1e2") == [-0.00011, 5.5, 210.0]


def test_inf():
    assert sparkline.guess_series("-inf +inf 1 2") == [
        float("-inf"),
        float("inf"),
        1.0,
        2.0,
    ]
