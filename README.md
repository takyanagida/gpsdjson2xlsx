gpsdjson2xlsx
=====================================

Reads GPSD JSON and format satellite signal information into Excel file (xlsx) like below.
First line is satellite's PRN IDs (virtually satellite numbers), numbers in later lines are S/N ratio. Green cell means that satellite signal is used for location calculation and gray is for unused.

![](https://github.com/takyanagida/gpsdjson2xlsx/blob/master/screenshot.png)

See http://takyanagida.com/gps-receiver-evaluation-methodology-and-tools.html for background and use case.

Dependencies
-----------------------------
- GPSD
- Python XlsxWriter

Usage
-----------------------------

    gpsfake -1 -p RAW.nmea | grep -e '^\{' | gpsdjson2xlsx.py

You can open generated xlsx file with LibreOffice Calc by the following command.

    libreoffice --calc output.xlsx

You can optionally set output filename:

    gpsfake -1 -p RAW.nmea | grep -e '^\{' | gpsdjson2xlsx.py COOKED.xlsx

License
-------------------------------

This software is licensed under CC0.
https://creativecommons.org/publicdomain/zero/1.0/
