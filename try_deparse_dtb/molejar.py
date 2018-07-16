
import fdt

#-----------------------------------------------
# convert *.dtb to *.dts
# ----------------------------------------------
with open("am335x-olimex-som-evb.dtb", "rb") as f:
  dtb_data = f.read()

dt1 = fdt.parse_dtb(dtb_data)

with open("am335x-olimex-som-evb.dts", "w") as f:
  f.write(dt1.to_dts())

#-----------------------------------------------
# convert *.dts to *.dtb
# ----------------------------------------------
with open("am335x-olimex-som-evb.dts", "r") as f:
  dts_text = f.read()

dt2 = fdt.parse_dts(dts_text)

with open("am335x-olimex-som-evb.dtb", "wb") as f:
  f.write(dt2.to_dtb(version=17))

#-----------------------------------------------
# Add Property and Node into dt2
# ----------------------------------------------
node = fdt.Node('test_node')
node.append(fdt.Property('basic_property'))
node.append(fdt.PropStrings('string_property', 'value1', 'value2'))
node.append(fdt.PropWords('words_property', 0x1000, 0x80000000, wsize=32))
node.append(fdt.PropBytes('bytes_property', data=[0, 200, 12]))
dt2.add_item(node)

#-----------------------------------------------
# merge dt2 into dt1
# ----------------------------------------------
dt1.merge(dt2)

with open("merged.dtb", "wb") as f:
  f.write(dt1.to_dtb(version=17))

#-----------------------------------------------
# diff two fdt objects
# ----------------------------------------------
out = fdt.diff(dt1, dt2)

print("-------------- SAME -------------")
print(out[0]) # same in dt1 and dt2
print("-------------- DT1 -------------")
print(out[1]) # specific for dt1
print("-------------- DT2 -------------")
print(out[2]) # specific for dt2
