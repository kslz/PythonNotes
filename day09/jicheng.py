class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age


if __name__ == "__main__":
    lizi = Person("lizi", 25)
    print(lizi.name)
    lizi.name = "lizi123"
    print(lizi.name)

if
