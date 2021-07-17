#!/usr/bin/env python3

import random, sys
if len(sys.argv) < 2:
    print("no size specified", file=sys.stderr)
    sys.exit(1)

size = [int(c) for c in sys.argv[1].split("x")]

if len(size) != 2:
    print("invalid size", file=sys.stderr)
    sys.exit(1)

value_range = [1, 6]
if len(sys.argv) > 2:
    value_range = [int(c) for c in sys.argv[2].split(":")]
    if len(value_range) != 2:
        print("invalid range", file=sys.stderr)
        sys.exit(1)

table = []
for y in range(size[1]):
    this_row = []
    for x in range(size[0]):
        this_row.append(random.randint(*value_range))
    table.append(this_row)

output_rows = []
for row in table:
    this_row = []
    for val in row:
        this_row.append(str(val))
    output_rows.append("\t".join(this_row))

print("\n".join(output_rows))
