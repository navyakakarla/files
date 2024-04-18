#append means will add in last#
n = [1,2,3,4,1234,2,'navya']
n.append("python")
print(n)
#extend we can add bulk #
n = [1,2,3,4,1234,2,'navya']
n.extend([4708848749])
print (n)
#count#
n = [1,2,3,4,1234,2,2,'navya']
print(n.count(2))
#remove#
n = [1,2,3,4,5,6]
n.remove(2)
print(n)
#pop means indexing from 0,1,2,3,4 #
n = [1,2,3,45,6]
n.pop(2)
print(n)
#index#
n = [1,2,3,4,5,6]
print(n.index(1))
#for loop#
for i in [1,2,3,4,5,6]:
    print(i)

