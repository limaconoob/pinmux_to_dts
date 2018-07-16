
#! /usr/bin/bash

#Converting official .dtb to json with pyfdt
python2.7 dtb_to_json.py am335x-olimex-som-evb.dtb >> am335x-olimex-som-evb.json

#Converting json file created above to dts with pyfdt
python2.7 json_to_dts.py am335x-olimex-som-evb.json >> am335x-olimex-som-evb.dts

#save file
mv am335x-olimex-som-evb.dtb save.dtb

#Try to reverse the process, to reconstitute the intial dtb from the dts file created above
#This step fail badly, the dts seems to be corrupted
##python2.7 dts_to_dtb.py am335x-olimex-som-evb.dts >> am335x-olimex-som-evb.dtb
dtc -I dts am335x-olimex-som-evb.dts -O dtb -o am335x-olimex-som-evb.dtb
