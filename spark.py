#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
import sys

spark_chars = u"▁▂▃▄▅▆▇█"

def convert_to_float(i):
    try:
        return float(i)
    except:
        return None

# Read all data from stdin, split by whitespace
series_data_raw = [ i.strip() for i in sys.stdin.read().split() ]

# Convert valid floats to float, discard remaining elements
series_data = filter(lambda x: x is not None, map(convert_to_float, series_data_raw))

maximum = max(series_data)

if maximum == 0.0:
    print "Cannot normalize when maximum is zero."
    sys.exit(1)

sparked_series_data = map(lambda x: spark_chars[int(x * 7 / maximum)], series_data)

print ''.join(sparked_series_data)
