#!/usr/bin/env python3.6

import argparse

import os
import sys

# defining y variables
domains = ['comodoca.net',
        'brad.dc.comodoca.net',
        'mcr.dc.comodoca.net',
        'sec.dc.comodoca.net',
        'as48477.net']

parser = argparse.ArgumentParser()

# By default it will fail with multiple arguments.
parser.add_argument('--default',
        default=domains[0:4],
        help='Show backups (ex: hostname.brad.dc.comodoca.net)')

# Telling the type to be a list will also fail for multiple arguments,
# but give incorrect results for a single argument.
#parser.add_argument('--list-type',
#        type=list
#        )
parser.add_argument('-i', '--item', action='store', dest='alist',
        type=str, nargs='*', default=(domains[:4]),
        help="Examples: -i item1 item2, -i item3")


opts = parser.parse_args()
#print(args.default)
print("List of items: {}".format(opts.alist))
