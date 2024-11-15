# context manager
# with - context manager
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', "w",
          encoding='utf-8') as fh:  # łapiemy do zmiennej fh filehandler jaki dostarcza system do komunikacji z plikiem
    fh.write("Powitanie\n")
    fh.write("Powitanie\n")
    fh.write("Powitanie\n")
    fh.write("kolejne\n")

with open('test.log', "w",
          encoding='utf-8') as fh:  # łapiemy do zmiennej fh filehandler jaki dostarcza system do komunikacji z plikiem
    fh.write("Nowy tekst\n")

with open('test.log', "a",
          encoding='utf-8') as fh:  # łapiemy do zmiennej fh filehandler jaki dostarcza system do komunikacji z plikiem
    fh.write("Dopisane\n")
    fh.write("Dośdane\n")

with open('test.log', "r",
          encoding='utf-8') as fh:  # łapiemy do zmiennej fh filehandler jaki dostarcza system do komunikacji z plikiem
    lines = fh.read()

print(lines)
