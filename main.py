a = 2
b = 3
c = 7

import sys
def printf(format, *args):
    sys.stdout.write(format % args)

printf('The answer is %r.\n', (a * b * c))
