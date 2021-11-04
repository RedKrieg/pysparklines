# vim: set fileencoding=utf-8 :
import math, os, re, string, sys

spark_chars = u"▁▂▃▄▅▆▇█"
"""Eight unicode characters of (nearly) steadily increasing height."""

def _convert_to_float(n):
    try:
        return float(n)
    except:
        return None

def _isan(n):
    return not math.isnan(n)

def sparkify(series, minimum=None, maximum=None):
    u"""Converts <series> to a sparkline string.
    
    Example:
    >>> sparkify([ 0.5, 1.2, 3.5, 7.3, 8.0, 12.5, float("nan"), 15.0, 14.2, 11.8, 6.1,
    ... 1.9 ])
    u'▁▁▂▄▅▇ ██▆▄▂'

    >>> sparkify([1, 1, -2, 3, -5, 8, -13])
    u'▆▆▅▆▄█▁'

    Raises ValueError if input data cannot be converted to float.
    Raises TypeError if series is not an iterable.
    """
    series = [ float(n) for n in series ]
    if all(math.isnan(n) for n in series):
        return u' ' * len(series)

    minimum = min(filter(_isan, series)) if minimum is None else minimum
    maximum = max(filter(_isan, series)) if maximum is None else maximum
    data_range = maximum - minimum
    if data_range == 0.0:
        # Graph a baseline if every input value is equal.
        return u''.join([ spark_chars[0] for i in series ])
    coefficient = (len(spark_chars) - 1.0) / data_range

    def clamp(n):
        return min(max(n, minimum), maximum)

    def spark_for(n):
        return spark_chars[int(round((clamp(n) - minimum) * coefficient))]

    return u''.join(spark_for(n) if _isan(n) else ' ' for n in series)


def guess_series(input_string):
    u"""Tries to convert <input_string> into a list of floats.

    Example:
    >>> guess_series("0.5 1.2 3.5 7.3 8 nan 12.5, 13.2,"
    ... "15.0, 14.2, 11.8, 6.1, 1.9")
    [0.5, 1.2, 3.5, 7.3, 8.0, nan, 12.5, 13.2, 15.0, 14.2, 11.8, 6.1, 1.9]
    """
    float_finder = re.compile(r"(nan|[-+]?[0-9]*\.?[0-9]+(?:e[-+]?[0-9]+)?)", re.I)
    return ([
        i for i in [
            _convert_to_float(j) for j in float_finder.findall(input_string)
        # Remove entires we couldn't convert to a sensible value.
        ] if i is not None and not math.isinf(i)
    ])

def main():
    u"""Reads from command line args or stdin and prints a sparkline from the
    data.  Requires at least 2 data points as input.
    """
    import argparse
    from pkg_resources import require

    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument(
        "data",
        nargs="*",
        help="Floating point data, any delimiter."
    )
    parser.add_argument(
        "--version",
        "-v",
        action="store_true",
        help="Display the version number and exit."
    )
    parser.add_argument(
        "--min",
        type=float,
        help="Set smaller values to MIN."
    )
    parser.add_argument(
        "--max",
        type=float,
        help="Set larger values to MAX."
    )
    args = parser.parse_args()
    
    if args.version:
        version = require("pysparklines")[0].version
        print(version)
        sys.exit(0)

    if os.isatty(0) and not args.data:
        parser.print_help()
        sys.exit(1)
    elif args.data:
        arg_string = u' '.join(args.data)
    else:
        arg_string = sys.stdin.read()

    try:
        print(sparkify(guess_series(arg_string), minimum=args.min, maximum=args.max))
    except:
        sys.stderr.write("Could not convert input data to valid sparkline\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
