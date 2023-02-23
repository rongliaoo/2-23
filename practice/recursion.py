'''
def power(r,n):
    value = 1
    for i in range(1,n+1):
        value = r*value
    return value
print(power(2,4))

'''
'''
def main():
    n = eval(input("input one number:"))

def factorial(n):
    value = 0
    for i in range(1,n+1):
        value = n - 1
        m = n*value
        #print(m)
    return n
print(m)
'''



def factorial_loop(n):
    factor = 1
    for i in range(1,n+1):
        factor *= i
    print(factor)
    return factor
n = eval(input("number:"))
factorial_loop(n)



def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n *factorial(n - 1)
n = eval(input("Number:"))
print(factorial(n))
