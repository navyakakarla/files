#can remove leading or trailing whitespaces in a string
name="hello world" .strip()
print(name)
#can remove any leading and trailing characters
name="###hello world###".strip('#')
print(name)
#
name=" ###hello world".strip('#')
print(name)
#capitals#
name="Hello World".strip('ldoH')
print(name)
#
name="Hello World".strip('ldoh')
print(name)