from queue import Queue
import inspect

q=Queue()
print(q)
print(inspect.getsource(Queue))
class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

qu=Queue()
print(qu)


class Person:
    def __init__(self,name):
        self.name=name

    def __repr__(self) -> str:
        return f"Person({self.name})"

    def __mul__(self,x):
        if type(x) is not int:
            raise Exception("invalid argument,must be int")
        self.name=self.name*x

    def __call__(self,y):
        print("called this function")


p=Person("tim")
print(p)#will print the memory address
p(4)

