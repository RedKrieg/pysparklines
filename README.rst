===========
pysparkline
===========

Python clone of https://github.com/holman/spark

Takes series data via stdin, command line, or API and prints a sparkline representation.

Output is always UTF-8 encoded.

Usage:

- $ ``sparkline 4 3 2 1``
  █▆▃▁
- $ ``echo "1.0 1.0 2.0 3.0 5.0 8.0 13.0" | sparkline``
  ▁▁▂▂▃▅█
- $ ``python -c "import sparkline; print sparkline.sparkify([1.0, 2.0, 3.0, 4.0]).encode('utf-8')"``
  ▁▃▆█
