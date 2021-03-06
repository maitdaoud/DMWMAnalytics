#!/usr/bin/env python
#-*- coding: utf-8 -*-
#pylint: disable=

"""
File       : dates.py
Author     : Valentin Kuznetsov <vkuznet AT gmail dot com>
Description: This module generates series of days in specific
interval starting from given date.
"""
from __future__ import print_function

# system modules
import sys
import optparse

# package modules
from DCAF.utils.utils import dates

class OptionParser():
    "User based option parser"
    def __init__(self):
        usage  = 'Usage: %prog [options]\n'
        usage += 'Description: prints weekly dates from given start date\n'
        usage += 'Example: %prog --start=20140101'
        self.parser = optparse.OptionParser(usage=usage)
        self.parser.add_option("--start", action="store", type="string", \
            dest="start", default="", help="Input start date (YYYYMMDD)")
        self.parser.add_option("--ndays", action="store", type="int", \
            dest="ndays", default=7, help="Dates interval, default 7 days")
        self.parser.add_option("--overlap", action="store_true", \
            dest="overlap", default=False, help="Overlap dates boundaries")
    def get_opt(self):
        "Return list of options"
        return self.parser.parse_args()

def main():
    "Main function"
    optmgr  = OptionParser()
    opts, _ = optmgr.get_opt()
    start_date = opts.start
    ndays = opts.ndays
    if  not start_date:
        print("Please specify start date, see --help for more options")
        sys.exit(1)
    for pair in dates(start_date, ndays, opts.overlap):
        print('%s %s' % (pair[0], pair[1]))

if __name__ == '__main__':
    main()
