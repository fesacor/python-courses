from string import Template

templ = Template('My name is ${author} and today I\'m feeling ${state}.')

data = {
    'author': 'Felipe',
    'state': 'happy'
}
str1 = templ.substitute(data)
print(str1)