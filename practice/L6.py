phoneBook = {"Alice":"123-4567","Bob":"987_6543"}
name = input("Enter the name:")
list = list(phoneBook)
#print(list)
for i in range(len(list)):
    if name == list[i]:
        print(phoneBook[name])
        answer = True
        break
    else:
        answer = False

if answer == False:
    print("Name not found.")

    


#print(phoneBook.keys())
'''
if name == phoneBook.keys():
    print(phoneBook[name])
else:
    print("Name not found.")
'''
'''


try:
    print(phoneBook[name])
except KeyError:
    print("Name not found.")


'''



