import re, os, sys, struct
os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))

minimum_number = number = 0xfeed0000
ch = open('config.h', 'w')
cah = open('config_asm.h', 'w')
cp = open('config.py', 'w')

for line in open('config.txt'):
    line = re.sub('//.*$', '', line).strip()
    if line == '': continue
    if line.startswith('#'): # a constant
        print >> ch, line
        print >> cah, line
        continue
    val = '0x%08x' % number
    number += 1
    print >> ch, 'static volatile const unsigned int %s = %s;' % (line, val)
    print >> cah, '#define %s %s' % (line, val)
    print >> cp, '%s = %s' % (line, val)
