pysparkline
====

Python 3 clone of [Zach Holman's BASH sparkline project](https://github.com/holman/spark)

Takes series data via stdin, command line, or API and prints a sparkline representation.

Usage:

- $ `sparkline 4 3 2 1`
  █▆▃▁
- $ `echo "1.0 1.0 2.0 3.0 5.0 8.0 13.0" | sparkline`
  ▁▁▂▂▃▅█
- $ `python3 -c "import sparkline; print(sparkline.sparkify([1.0, 2.0, 3.0, 4.0]))"`
  ▁▃▆█
