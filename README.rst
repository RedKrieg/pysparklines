========
spark.py
========

Python clone of https://github.com/holman/spark

Takes series data via stdin and prints a sparkline representation.

Utilizes utf-8 encoded characters in output.

Usage:

- $ ``sparkline 4 3 2 1``
  █▆▃▁
- $ ``echo "1.0 1.0 2.0 3.0 5.0 8.0 13.0" | sparkline``
  ▁▁▂▂▃▅█
- $ ``python -c "import sparkline; print sparkline.sparkify([1.0, 2.0, 3.0, 4.0]).encode('utf-8')"``
  ▁▃▆█
