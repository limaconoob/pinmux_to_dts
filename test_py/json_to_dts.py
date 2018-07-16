
from pyfdt.pyfdt import FdtJsonParse

with open("./am335x-evm.json") as bonjour:
  coucou = FdtJsonParse(bonjour)
  print coucou.to_dts()
 

