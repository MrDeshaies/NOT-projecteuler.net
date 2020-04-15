
def changex(x):
    x += 1
    x = 3
x=1
changex(x)
print(x)

def changelist(x):
    x.append(5)
    x = [i ** 2 for i in x]
    # for i in range(len(x)):
    #     x[i] *= 2

x = [1,2,3,4]
changelist(x)
print(x)

class Car:
    pass

def changecar(x):
    x.wheels *= 2
x = Car()
x.wheels = 2
print(x.wheels)
changecar(x)
print(x.wheels)