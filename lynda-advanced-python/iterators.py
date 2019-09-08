from string import Template

days_english = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
days_spanish = ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab']

days_eng_i = iter(days_english)
eng_day_1 = next(days_eng_i)
eng_day_2 = next(days_eng_i)
days_spa_i = iter(days_spanish)

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