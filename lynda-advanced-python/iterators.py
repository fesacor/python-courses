from string import Template

days_english = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
days_spanish = ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab']

days_eng_i = iter(days_english)
eng_day_1 = next(days_eng_i)
eng_day_2 = next(days_eng_i)

print('Enumerated days in Spanish:')
# Use start=1 to start on index '1'
for i, d in enumerate(days_spanish, start=1):
    print('\t{} {}'.format(i, d))

print('Days in English and Spanish:')
for d in zip(days_english, days_spanish):
    print('\tEnglish: {}, Spanish: {}.'.format(d[0], d[1]))

with open('iterators.txt', 'r') as f:
    # Sentinel value passed to iter is an empty string
    # which denotes the end of the file.
    print('iterators.txt contents:')
    for l in iter(f.readline, ''):
        print('\t{}'.format(l))

templ_str = (
    'days_english: ${days_english}\n'
    'days_spanish: ${days_spanish}\n\t'
    '- English day 1: ${eng_day_1}\n\t'
    '- English day 2: ${eng_day_2}'
)
templ = Template(templ_str)
results = {
    'days_english': days_english,
    'days_spanish': days_spanish,
    'eng_day_1': eng_day_1,
    'eng_day_2': eng_day_2
}
print(templ.substitute(results))