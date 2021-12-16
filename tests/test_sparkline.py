# vim: set fileencoding=utf-8 :
import pytest
import sparkline


def test_1234():
    assert sparkline.sparkify([1, 2, 3, 4]) == u"▁▃▆█"


def test_range_8():
    assert sparkline.sparkify(range(8)) == u"▁▂▃▄▅▆▇█"


def test_range_9():
    assert sparkline.sparkify(range(9)) == u"▁▂▃▄▅▅▆▇█"


def test_inf():
    assert sparkline.sparkify([float("-inf"), 0, float("inf")]) == u" ▁ "


def test_nan():
    assert sparkline.sparkify([float("nan"), 0, 1]) == u" ▁█"


def test_fib():
    assert sparkline.sparkify([1.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0]) == u"▁▁▂▂▃▅█"


def test_multiline():
    import math

    assert (
        sparkline.sparkify([math.cos(n / 10.0) for n in range(-50, 50, 2)], rows=4)
        == u"""                    ▁▃▅▇███▇▅▃▁                   
▅▂                ▃▆███████████▆▃                ▂
██▇▄▁          ▂▅█████████████████▅▂          ▁▄▇█
█████▆▄▃▁▁▁▂▃▅▇█████████████████████▇▅▃▂▁▁▁▃▄▆████"""
    )
