import os
import time
merah = "\033[1;31m"
kuning = "\033[1;33m"
hijau = "\033[1;32m"
biru = "\033[1;34m"
ungu = "\033[1;35m"
putih = "\033[1;37m"
reset = "\033[0;0m"

baris = 14
kolom = 30
pad = 0
inout = False
while True:
    # os.system("clear")

    for i in range(baris):
        for j in range(kolom):
            if i < pad or i >= baris - pad or j < (pad * 2) or j >= kolom - (pad * 2):
                val = merah
            else:
                val = biru
            print(val + "x", end=reset)
        print()

    if inout:
        pad -= 1
        if pad < 0:
            inout = False
    else:
        pad += 1
        if pad > baris/2:
            inout = True

    time.sleep(0.1)
    

#   +++++++++++++++
#   +++++++++++++++
#   +++++++++++++++
#   ---------------
#   ---------------
#   ---------------

#   +++++++++++++++
#   +.............+
#   +.............+
#   +.............+
#   +.............+
#   +++++++++++++++

# pad = 1

# for i in range(baris):
#     for j in range(kolom):
#         if i < pad or i >= baris - pad or j < (pad * 2) or j >= kolom - (pad * 2):
#             val = merah
#         else:
#             val = biru
#         print(val + "x", end=reset)
#     print()

#   +
#   ++
#   +++
#   ++++
#   +++++
#   ++++++
#   +++++++
#   ++++++++
#   +++++++++
