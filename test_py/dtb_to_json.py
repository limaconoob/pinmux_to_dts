
from pyfdt.pyfdt import FdtBlobParse

with open("../sdk_device_tree/am335x-evm.dtb") as bonjour:
  dtb = FdtBlobParse(bonjour)
  print dtb.to_fdt().to_json()
 

