
#! /usr/bin/bash
python2.7 dtb_to_json.py am335x-olimex-som-evb.dtb >> am335x-olimex-som-evb.json
python2.7 json_to_dts.py am335x-olimex-som-evb.json >> am335x-olimex-som-evb.dts
mv am335x-olimex-som-evb.dtb save.dtb
##python2.7 dts_to_dtb.py am335x-olimex-som-evb.dts >> am335x-olimex-som-evb.dtb
dtc -I dts am335x-olimex-som-evb.dts -O dtb -o am335x-olimex-som-evb.dtb
