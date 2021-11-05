pysparkline
====

Python 3 clone of [Zach Holman's BASH sparkline project](https://github.com/holman/spark)

Takes series data via stdin, command line, or API and prints a sparkline representation.

Usage:

- $ `sparkline 4 3 2 1`
```
█▆▃▁
```
- $ `echo "1.0 1.0 2.0 3.0 5.0 8.0 13.0" | sparkline`
```
▁▁▂▂▃▅█
```
- $ `seq 20 | sort -R | sparkline -r2`
```
▃▁ █▂    ▂▆▅  ▄▇▆   
██▃██▅▇▄▁███▃▇███▂█▆
```
- $ `python3 -c "import sparkline; print(sparkline.sparkify([1.0, 2.0, 3.0, 4.0]))"`
```
▁▃▆█
```
- $ `python3 -c "import math, sparkline; print(sparkline.sparkify([math.cos(n/10.0) for n in range(-50, 50, 2)], rows=4))"`
```
                    ▁▃▅▇███▇▅▃▁                   
▅▂                ▃▆███████████▆▃                ▂
██▇▄▁          ▂▅█████████████████▅▂          ▁▄▇█
█████▆▄▃▁▁▁▂▃▅▇█████████████████████▇▅▃▂▁▁▁▃▄▆████
```
