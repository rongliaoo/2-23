def main():
    file = 'Greeting.txt'
    displaywithForLoop(file)
    print()
    displaywithcomprehensionside(file)
    createdictionary(file)
    createDictionary(file)

def displaywithForLoop(file):
    infile = open(file, 'r')
    for line in infile:
        print(line, end= '')
    infile.close

def displaywithcomprehensionside(file):
    infile = open(file, 'r')
    list = [line.rstrip() for line in infile]
    infile.close
    print(list) 

def createdictionary(file):
    infile = open(file,'r')
    dictionary = {line.split(",")[0]:line.split(',')[1] .rstrip() for line in infile}
    print(dictionary)

def createDictionary(file):
    infile = open(file, 'r')
    textList = [line.rstrip() for line in infile]
    print(textList)
    print(' '.join(textList))
    print(','.join(textList))
    infile.close()
    print(dict([x.split(',') for x in textList]))

main()