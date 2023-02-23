'''
def main():
    print(repeatLastLetter("oprah"))

def repeatLastLetter(w):
    if len(w) == 1:
        return w
    else:
        print(repeatLastLetter(w[1:]) + repeatLastLetter(w[1:]))
        return repeatLastLetter(w[1:]) + repeatLastLetter(w[1:])

main()
'''

def main():
    print(repeatLastLetter("oprah"))

def repeatLastLetter(w):
    if len(w) == 1:
        return w
    else:
        print(repeatLastLetter(w[1:]) + repeatLastLetter(w[1:]))
        return repeatLastLetter(w[1:]) + repeatLastLetter(w[1:])

main()


