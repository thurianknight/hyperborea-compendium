# The following code will search '"_id":"*",' (e.g. '"_id":"0N2M1yQAzc4enzOf",' ),
# and replace with Null in multi-line mode.

import re

input_file = open("./packs/actor-2-bestiary-1.db", "r")
output_file = open("./packs/actor-2-bestiary-1.db.out", "w")
br = 0
ot = 0

for line in input_file:
    match_br = re.match(r'\s*#define .*_BR (0x[a-zA-Z_0-9]{8})', line) # Should be your regular expression
    match_ot = re.match(r'\s*#define (.*)_OT (0x[a-zA-Z_0-9]+)', line) # Second regular expression

if match_br:
    br = match_br.group(1)
    # Do something

elif match_ot:
    ot = match_ot.group(2)
    # Do your replacement

else:
    output_file.write(line)