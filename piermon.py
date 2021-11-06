#!/usr/bin/env python

import subprocess as sp
import datetime as dt
import argparse as ap
import os

def main():
    argp = ap.ArgumentParser()
    argp.add_argument("-i", "--indir", type=str, help="Pier directory")
    argp.add_argument("-o", "--outfile", type=str, help="CSV to write to")
    args = argp.parse_args()
    s = int(sp.check_output(['du', '-s',
                             args.indir]).decode('ascii').split()[0])
    if not os.path.exists(args.outfile):
        with open(args.outfile, 'a') as f:
            f.write(f"datetime_utc,piersize_bytes\n")
    with open(args.outfile, 'a') as f:
        f.write(f"{dt.datetime.utcnow()}, {s}\n")

if __name__ == "__main__":
    main()

