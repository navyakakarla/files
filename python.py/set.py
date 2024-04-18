#set type check we need to allow vales#
s = {1,2,3}
print(type(s))
#dont allow duplicates#
s = {1,2,3,4,4,3,2,1}
print(s)
#unorderd#
s = {1,7,8,5,24,67,3,9}
print(s)
#add,update,pop,remove#
#pop will randomly will delete because unordered#
s = {1,2,3,9,8,7}
s.add(123)
print(s)
#update bulk data we can add#
s = {1,2,3,9,8,7}
s.update({5,6,56,78})
print(s)
#pop will randomly will delete because unordered#
s = {1,2,3,9,8,7}
s.pop()
print(s)
#remove#
s = {1,2,3,9,8,7}
s.remove(2)
print(s)
#set operations union,intersection,difference,is subset,is superset#
#union all number will get#
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.union(set2))
#intersection common nunbers#
set1 = {1,2,3,4}
set2 = {4,5,6}
print(set1.intersection(set2))
#difference#
set1 = {1,2,3,4}
set2 = {4,5,6}
print(set1.difference(set2))
#superset want to get set1 and set2 same numbers#
set1 = {1,2,3,4,5,6}
set2 = {4,5,6}
print(set1.issuperset(set2))
#subset is also same#
set1 = {1,2,3,4,5,6}
set2 = {4,5,6}
print(set2.issubset(set1))
#for#
for i in {1,2,3,4}:
    print(i)