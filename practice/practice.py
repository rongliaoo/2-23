'''
outfile = open("Greetings.txt","w")
outfile.write("Hello\n")
outfile.write("Aloha\n")
outfile.write("Aloha\n")
outfile.close()

infile = open("Greetings.txt","r")

for line in infile:
    text = infile.readline().rstrip()
infile.close()
print(text)

#.rstrip()
#print(infile.readline().rstrip())
'''

infile = open("Greetings.txt","r")
for line in infile.readline():
    print(line)
infile.close()

'''
infile = open("Greetings.txt","r")
for line in infile:
    text = infile.read()
    #print(line)
    print(text)
infile.close()
'''