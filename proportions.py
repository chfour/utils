#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print(f"{sys.argv[0]} 1:2:3 =6", file=sys.stderr)
    sys.exit(1)

props = [float(i) for i in sys.argv[1].split(":")]
to_split = sys.argv[2].split(":")
if len(to_split) < 2:
    to_split.append(sys.argv[2])
    to_split[0] = None
elif not to_split[0]:
    to_split[0] = None
else:
    to_split[0] = int(to_split[0])
to_split[1] = float(to_split[1])

print(" : ".join([str(i) for i in props]) + " / " + str(sys.argv[2]))
#print(" : ".join([f"{i}/{sum(props)}" for i in props]))

if to_split[0] is None: to_split = to_split[1]
else:
    to_split = props[to_split[0]] / to_split[1] * sum(props)

print(to_split)

for i in props:
    this_item = i / sum(props) * to_split
    print(f"{i}/{sum(props)} * {to_split} = {this_item}")
