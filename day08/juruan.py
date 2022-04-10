class Juruan(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def whatage(self):
        print(self._age)


def main():
    juruan01 = Juruan("j1", 20)
    juruan01.whatage()
    juruan01.age = 25
    juruan01.whatage()
    juruan01.havell = True
    print(juruan01.havell)
    print(juruan01.age)

if __name__ == '__main__':
    main()
