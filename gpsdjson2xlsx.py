#!/usr/bin/env python3
#
# gpsdjson2xlsx -- format GPSD JSON satellite information
#                  into human-readable Excel table
#
# Written by Tak Yanagida
#
# This file is licensed under CC0.
# https://creativecommons.org/publicdomain/zero/1.0/

import sys
import argparse
import json
import xlsxwriter

parser = argparse.ArgumentParser()
parser.add_argument('input', type=argparse.FileType(), nargs='?', default=sys.stdin)
parser.add_argument('output', nargs='?', default='out.xlsx')
args = parser.parse_args()

workbook = xlsxwriter.Workbook(args.output)
worksheet = workbook.add_worksheet()
used_style = workbook.add_format({'bg_color': '#80ff80'})
notused_style = workbook.add_format({'bg_color': 'gray'})

msgs = []

for line in args.input:
    msg = json.loads(line)
    msgs.append(msg)

satellites = set()
for msg in msgs:
    if (msg['class'] != "SKY"):
        continue
    for sat in msg['satellites']:
        satellites.add(sat['PRN'])

fields = sorted(list(satellites))
row = 0
column = 0
for field in fields:
    worksheet.write(row, column, field)
    column += 1

row = 1
column = 0
for msg in msgs:
    snr = {}
    if (msg['class'] != "SKY"):
        continue
    for sat in msg['satellites']:
        column = fields.index(sat['PRN'])
        if (sat['used'] == True):
            worksheet.write(row, column, sat['ss'], used_style)
        elif (sat['used'] == False):
            worksheet.write(row, column, sat['ss'], notused_style)
        else:
            worksheet.write(row, column, sat['ss'])
    row += 1
    
workbook.close()
