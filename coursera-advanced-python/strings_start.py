b = bytes([0x41, 0x42, 0x43, 0x44])
print('Value of b: {}'.format(b))

s = 'This is a string.'
print(s)

try:
    print(s+b)
except Exception as e:
    print('Tried to do \'s+b\' but the error was: {}'.format(e))
    s2 = b.decode('utf-8')
    print('Decoded \'b\', This is the new concat result: {}'.format(s+s2))