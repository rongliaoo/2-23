def main():
    name = input("Enter person's name:")
    hours = eval(input("Enter number of hours worked:"))
    wage = eval(input("Enter houtly wage:"))
    #print(Wages(name,hours,wage).payForWeek())
    put = Wages(name,hours,wage)
    print("Pay for ", name,":${0:.2f}".format(put.payForWeek()))

class Wages:
    def __init__(self,name = '',hours = 0,wage = 0):
        self._name = name
        self._hours = hours
        self._wage = wage

    def payForWeek(self):
        if self._hours <= 40:
            return self._hours * self._wage
        else:
            return 40 * self._wage + (self._hours - 40)* self._wage * 1.5 
    
   # def __str__(self):
       # return str(self.payForWeek())

main()
print()






