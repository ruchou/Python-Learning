
# refer to https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make
# Common Mistake #1: Misusing expressions as defaults for function arguments '''
def foo(bar=[]):
    bar.append(10)
    print(bar)
for i in range(10):
    foo()

def foo1(bar=None):
    if bar==None:
        bar=[]
        bar.append(10)

#Common Mistake #2: Using class variables incorrectly'''

class A(object):
    x=1
class B(A):
    pass
class C(A):
    pass

print(A.x,B.x,C.x)

B.x=19
print(A.x,B.x,C.x)


A.x=2
print(A.x,B.x,C.x) #A.x changes and C.x also changes


# Common Mistake #3: Specifying parameters incorrectly for an exception block
try:
    l= ["a", "b"]
    int(l[2])
except(ValueError,IndexError) as e:
    pass


# Common Mistake #4: Misunderstanding Python scope rules
    x=10
    def foo():
        global x # supposed to add global
        x+=1
        print(x)
    foo()

#Common Mistake #5: Modifying a list while iterating over it
odd = lambda x : bool(x % 2)
numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if odd(numbers[i]):
        pass
       # del numbers[i]

# list comprehension
numbers[:]=[n for n in numbers if not odd(n)]
print(numbers)


# Common Mistake #6: Confusing how Python binds variables in closures
def create_multipliers():
    return [lambda x: i * x for i in range(5)]
    #late binding

for multiplier in create_multipliers():
    print(multiplier(2))
    # 8 8 8 8 8

def create_multipliers():
    return [lambda x, i=i: i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))
    # 0 2 4 6 8


for multiplier in (lambda x : i * x for i in range(5)):
    print(multiplier(2))
    #0 2 4 6 8

def create_multipliers():
    for i in range(5):
        yield lambda x: i * x
for multiplier in create_multipliers():
    print(multiplier(2))
    # 0 2 4 6 8
#https://www.getit01.com/p20180120329483144/
#https://www.zhihu.com/question/29483144
#https://itw01.com/VVIQ6E9.html

'''
This happens due to Python’s late binding behavior which says that the values of variables used in closures are looked up at the time the inner function is called. 
'''
