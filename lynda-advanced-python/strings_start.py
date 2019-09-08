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

b2 = s.encode('utf-8')
print('Encoding \'s\' as \'b2\' and doing \'b+b2\'. This is the result: {}'.format(b+b2))

b3 = s.encode('utf-32')
print('Encode \'s\' as utf-32. This is the result: {}'.format(b3))