
from pyfdt.pyfdt import FdtJsonParse
import sys

with open(sys.argv[1]) as bonjour:
  coucou = FdtJsonParse(bonjour)
  print coucou.to_dts()
 

