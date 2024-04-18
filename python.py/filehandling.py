#read mode#
s=open('demo.txt',mode='r')
print(s.read())
s.close()
#write mode we have demo.txt previously will get hello navya in write mode now will get bye bye that is trancate#
s=open('demo.txt',mode='w')
s.write("bye bye")
s.close()
#we need to append now for same thing
s=open('demo.txt',mode='a')
s.write("bye bye write")
s.close()
#read write
s=open('demo.txt',mode='r+')
print(s.read())
s.write("r+ mode")
s.close()
#write read#
s=open('demo.txt',mode='w+')
s.write("w+ mode")
s.seek(0)
print(s.read())
