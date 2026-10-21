# vim: set fileencoding=utf-8 :
import pytest
import sparkline


def test_1234():
    assert sparkline.sparkify([1, 2, 3, 4]) == "▁▃▆█"


def test_range_8():
    assert sparkline.sparkify(range(8)) == "▁▂▃▄▅▆▇█"


def test_range_9():
    assert sparkline.sparkify(range(9)) == "▁▂▃▄▅▅▆▇█"


def test_inf():
    assert sparkline.sparkify([float("-inf"), 0, float("inf")]) == " ▁ "


def test_nan():
    assert sparkline.sparkify([float("nan"), 0, 1]) == " ▁█"


def test_all_nan_or_inf():
    assert sparkline.sparkify([float("nan"), float("-inf")]) == "  "


def test_min():
    assert sparkline.sparkify([1, 2, 3, 4], minimum=2) == "▁▁▅█"


def test_max():
    assert sparkline.sparkify([1, 2, 3, 4], maximum=3) == "▁▅██"


def test_min_max():
    assert sparkline.sparkify([1, 2, 3, 4], minimum=2, maximum=3) == "▁▁██"


def test_fib():
    assert sparkline.sparkify([1.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0]) == "▁▁▂▂▃▅█"


def test_multiline():
    import math

    assert (
        sparkline.sparkify([math.cos(n / 10.0) for n in range(-50, 50, 2)], rows=4)
        == """                    ▁▃▅▇███▇▅▃▁                   
▅▂                ▃▆███████████▆▃                ▂
██▇▄▁          ▂▅█████████████████▅▂          ▁▄▇█
█████▆▄▃▁▁▁▂▃▅▇█████████████████████▇▅▃▂▁▁▁▃▄▆████"""
    )
