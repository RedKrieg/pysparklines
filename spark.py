#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
import math, re, string, sys

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
    coefficient = (len(spark_chars) - 1) / data_range
    return u''.join(
        map(
            lambda x: spark_chars[int(round((x - minimum) * coefficient))],
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
        # Remove entires we couldn't convert
        lambda x: x is not None and not math.isnan(x) and not math.isinf(x),
        map(
            _convert_to_float, # Function to convert to float
            float_finder.findall(input_string)
        )
    )

if __name__ == "__main__":
    print sparkify(guess_series(sys.stdin.read()))
