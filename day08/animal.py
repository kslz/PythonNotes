class Animal(object):
    '''这是父类'''

    def __init__(self, name='some_animal'):
        self._name = name
        print('父类构造函数')

    def speak(self):
        print('父类speak')


class Dog(Animal):
    # def __init__(self, name='some_dog'):
    #     self._name = name
    #     print('子类构造函数')

    def speak(self):
        print('子类speak')


def main():
    print('hello')
    an1 = Animal()
    an1.speak()

    dg1 = Dog()
    dg1.speak()


if __name__ == '__main__':
    main()
