import pytest
import runpy
import sparkline


def test_min_max(capsys):
    sparkline.main("--min 2 --max 7 0 1 2 3 4 5 6 7 8 9 10".split())
    captured = capsys.readouterr()
    assert captured.out == u"▁▁▁▂▄▅▇████\n"


def test_rows(capsys):
    sparkline.main("--rows 3 0 1 2 3 4 5 6 7 8 9 10".split())
    captured = capsys.readouterr()
    assert (
        captured.out
        == u"""       ▁▃▆█
    ▂▅▇████
▁▃▆████████
"""
    )
