
ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 212]

c2f = map(lambda t: (t-32) * 5/9, ftemps)
f2c = map(lambda t: (t * 9/5) + 32, ctemps)

print('Celsius to Farenheit:')
for i in zip(ctemps, c2f):
    print('\t{} -> {}'.format(i[0], i[1]))

print('Farenheit to Celsius:')
for i in zip(ftemps, f2c):
    print('\t{} -> {}'.format(i[0], i[1]))