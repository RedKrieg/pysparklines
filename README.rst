========
spark.py
========

Python clone of https://github.com/holman/spark

Takes series data via stdin and prints a sparkline representation.

Utilizes utf-8 encoded characters in output.

Usage: ``sparkline 1 2 3 4``
Or: ``echo "1.1 2.2 3.3 4.4" | sparkline``
Or: ``import spark; print sparkify([1.0, 2.0, 3.0, 4.0]).encode('utf-8')``
