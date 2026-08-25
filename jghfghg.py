class Addition:
    def __init__(self,n):
        self.n=n
    def __add__(self,second):
        return self.n + second.n

a1=Addition(10)
a2=Addition(20)
print(a1+a2)
