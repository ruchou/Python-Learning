
'mistake 1'
def foo(bar=[]):
    bar.append(10)
    print(bar)
for i in range(10):
    foo()

def foo1(bar=None):
    if bar==None:
        bar=[]
        bar.append(10)
        