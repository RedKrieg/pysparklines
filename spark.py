#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
import math, os, re, string, sys

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

def main():
    u"""Reads from command line args or stdin and prints a sparkline from the
    data.  Requires at least 2 data points as input.
    """
    import argparse

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument(
        "data",
        nargs=argparse.REMAINDER,
        help="Floating point data, any delimiter."
    )
    args = parser.parse_args()
    
    if os.isatty(0) and not args.data:
        parser.print_help()
        sys.exit(1)
    elif args.data:
        arg_string = u' '.join(args.data)
        output = sparkify(guess_series(arg_string))
    else:
        output = sparkify(guess_series(sys.stdin.read()))

    print output.encode('utf-8', 'ignore')

if __name__ == "__main__":
    main()
