from string import Template

list1 = [1, 2, 3, 0, 5, 6]
any1 = any(list1)
all1 = all(list1)
min1 = min(list1)
max1 = max(list1)
sum1 = sum(list1)

templ_str = (
    'list1 values: ${lvalues}\n\t'
    '- any(list1) = ${any}\n\t'
    '- all(list1) = ${all}\n\t'
    '- min(list1) = ${min}\n\t'
    '- max(list1) = ${max}\n\t'
    '- sum(list1) = ${sum}'
)
templ = Template(templ_str) 
results = {
    'lvalues': list1,
    'any': any1,
    'all': all1,
    'min': min1,
    'max': max1,
    'sum': sum1
}
print(templ.substitute(results))