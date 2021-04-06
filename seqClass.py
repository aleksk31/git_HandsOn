#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser
# importing the librarys

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
# check for input
args = parser.parse_args()
# parse, parse , sparse
args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence isnt DNA nor RNA')
if args.motif:
  args.motif = args.motif.upper()
  print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
  if re.match(args.motif, args.seq):
    print("FOUND")
  else:
    print("NOT FOUND")

# please read moar

