# code 1
# command to take multiple input
li1=[int(i) for i in input('Enter multiple Numbers: ').split()]
def fun(n1):
    return n1%3==0 and n1%5==0
# command to print filtered number divisible by 3 and 5
print(list(filter(fun,li1)))


# code 2
# command to print list of 1-100 numbers
li2=list(range(1,100))
def fun(n2):
    return n2%3==0 and n2%5==0
# command to print filtered number from 1-100 divisible by 3 and 5
print(list(filter(fun,li2)))
