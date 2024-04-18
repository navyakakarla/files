#dictionary type#
s = {}
print(type(s))
#
s = {1:'abc',22:'navya','python':1}
print(s[22])
#methods,get update,vaules,keys,items#
#get #
s = {1:'abc',22:'navya','python':1}
print(s.get(1))
#(keys)#
s = {1:'abc',22:'navya','python':1}
print(s.keys())
#vales#
s = {1:'abc',22:'navya','python':1}
print(s.values())
#items#
s = {1:'abc',22:'navya','python':1}
print(s.items())
#update#
s = {1:'abc',22:'navya','python':1}
s.update({1111:2222})
print(s)

