import os
f0 = 'G8_leaders3'
try:
    # Optain file stats and make decision
    s = os.stat(f0)
    if s.st_size == 0:
        raise OSError("File Size is Zero!")
        #print("file size is zero!")
except OSError:
    print("can not open file ",f0)

