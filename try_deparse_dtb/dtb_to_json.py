
from pyfdt.pyfdt import FdtBlobParse
import sys

with open(sys.argv[1]) as bonjour:
  dtb = FdtBlobParse(bonjour)
  print dtb.to_fdt().to_json()
 

