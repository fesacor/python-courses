from string import Template

templ = Template('My name is ${author}.')

str1 = templ.substitute(author='Felipe')
print(str1)