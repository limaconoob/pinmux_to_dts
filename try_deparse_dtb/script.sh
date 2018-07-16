
#! /usr/bin/bash

#Converting an official dtb to a dts with pyfdt (Molejar)
python molejar.py

#Save original file
mv am335x-olimex-som-evb.dtb save.dtb

#Reverse the process, to reconstitute the intial dtb from the dts file created above
#Needs an on-board test
#This step seems working but has many Warnings like :
##  - am335x-olimex-som-evb.dtb: Warning (unit_address_vs_reg): Node /ocp/l4_wkup@44c00000/prcm@200000/clocks/stm_clk_div_ck has a reg or ranges property, but no unit name
##  - am335x-olimex-som-evb.dtb: Warning (unit_address_vs_reg): Node /leds/led@0 has a unit name, but no reg property
##  - am335x-olimex-som-evb.dtb: Warning (simple_bus_reg): Node /ocp/mcasp@4803C000 simple-bus unit address format error, expected "4803c000"
##  - am335x-olimex-som-evb.dtb: Warning (phys_property): Missing property '#phy-cells' in node /ocp/usb@47400000/usb-phy@47401300 or bad phandle (referred from /ocp/usb@47400000/usb@47401000:phys[0])
dtc -I dts am335x-olimex-som-evb.dts -O dtb -o am335x-olimex-som-evb.dtb
