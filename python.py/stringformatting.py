#%-formatting#
name="jaspreet"
print("my name is %s." % name)
#multiple varaiables allowed
name="jaspreet"
city="ongole"
print("my name is %s and i live in %s."%(name,city))
#str.format()function placeholders are replaced by curly bases
name="jaspreet"
city="ongole"
print("my name is {} and i live in {}.". format(name,city))
#referencing variables through indexing is possible
name="jaspreet"
city="ongole"
print("my name is {0} and i live in {1}.". format(name,city))
#To improve the readability,keywords cab be used
n="jaspreet"
c="ongole"
print("my name is {name} and i live in {city}.".format(name=n,city=c))