path = 'tired.txt'
f = open(path, 'w')
#lines = ['Hello World\n','123','456\n','789\n']
f.write('Hello World\n')
f.write('123\n')
f.write('456\n')
f.close()

infile = open('tired.txt','r')

#print([line.rstrip() for line in infile])
for line in infile:
   print(line)
