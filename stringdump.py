import sys
import re

chars = r"A-Za-z0-9/\-:.,_$%'()[\]<> "
shortest_run = 4

regexp = '[%s]{%d,}' % (chars, shortest_run)
pattern = re.compile(regexp)

def strings(stream):
    data = stream.read()
    return pattern.findall(data)

if __name__ == "__main__":
  
    file = open(sys.argv[1],'rb')
    
    for found_str in strings(file):
        print found_str