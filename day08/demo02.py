class Test:
    def prt(self):
        print(1)
        print(self)
        print(2)
        print(self.__class__)
        print(3)


t = Test()
print(123)
t.prt()