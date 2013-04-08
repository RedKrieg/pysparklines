#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
import re, string, sys

spark_chars = u"▁▂▃▄▅▆▇█"

def _convert_to_float(i):
    try:
        return float(i)
    except:
        return None

def sparkify(series):
    u"""Converts <series> to a sparkline string.
    
    Example:
        Input: [ 0.5, 1.2, 3.5, 7.3, 8.0, 12.5, 13.2,
                15.0, 14.2, 11.8, 6.1, 1.9 ]
        Output: ▁▁▂▄▅▇▇██▆▄▂
    """
    minimum = min(series)
    maximum = max(series)
    data_range = maximum - minimum

    if data_range == 0.0:
        raise Exception("Cannot normalize when range is zero.")

    return ''.join(
        map(
            lambda x: spark_chars[int(round((x - minimum) * 7.0 / data_range))],
            series
        )
    )

def guess_series(input_string):
    u"""Tries to convert <input_string> into a list of floats.

    Example:
        Input: "0.5 1.2 3.5 7.3 8 12.5, 13.2, 15.0, 14.2, 11.8, 6.1, 1.9"
        Output: [ 0.5, 1.2, 3.5, 7.3, 8.0, 12.5, 13.2,
                15.0, 14.2, 11.8, 6.1, 1.9 ]
    """
    float_finder = re.compile("([-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?)")
    return filter(
        lambda x: x is not None, # Remove entires we couldn't convert
        map(
            _convert_to_float, # Function to convert to float
            float_finder.findall(input_string)
        )
    )

if __name__ == "__main__":
    print sparkify(guess_series2(sys.stdin.read()))
