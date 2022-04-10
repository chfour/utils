#!/usr/bin/env python3
# a thing to dump everything from rtl_433's json output
# that has a temperature_C into a .csv file
# can be used to make pretty graphs out of temperature
# sensors in your area

# IMPORTANT: replace first line of output with last line of stderr

import json, fileinput, traceback, sys

sensor_names = []
count_total = count_filtered = 0
print("placeholder,placeholder2")
for l in fileinput.input():
    try:
        count_total += 1
        packet = json.loads(l)
        if "temperature_C" not in packet:
            continue
        count_filtered += 1

        name = f"{packet['model']}-{packet.get('id', '?')}-{packet.get('channel', '?')}"
        if name not in sensor_names:
            sensor_names.append(name)
        line = [""] * (1+1+sensor_names.index(name))
        line[0] = packet["time"]
        line[-1] = str(packet["temperature_C"])
        print(",".join(line))
    except:
        print(traceback.format_exc(), file=sys.stderr)
        print(packet, file=sys.stderr)
        exit(1)

print(f"{count_filtered}/{count_total}", file=sys.stderr)
print(" ".join(sensor_names), file=sys.stderr)
