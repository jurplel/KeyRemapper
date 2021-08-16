import plistlib

file = open("usb_hid_usages", "r", encoding='latin-1')

data = dict()

for line in file:
    if len(line) <= 0:
        continue

    if not line[0] == "\t":
        continue

    line = line.strip()
    
    if not line[0:2] == "0x":
        continue

    if line[4] == "-":
        continue

    line = line.split("\t")
    data[line[0]] = line[1]

plist = plistlib.dumps(data)

new_file = open("hid.plist", "wb")

new_file.write(plist)

new_file.close()

file.close()