# Exercise: Learn how to monkeypatch stuff: 
# http://en.wikipedia.org/wiki/Monkey_patch

class DonkeyKong(object):
    pass


def coconut_cannon(self):
    print('This monkeypatched method provided by Funky Kong')
    print(self)


# it's a pun -- a bad one
def fauxconut_cannon(self):
    print('This monkeypatched method provided by King K. Rool')
    print(self)


def monkeypatch_class(cls, method):
    # can't directly update __dict__ of a class, setattr is used instead
    # with the __name__ of the method to be added to the class.
    # see: 
    # http://stackoverflow.com/questions/20019333/modify-class-dict-mappingproxy-in-python

    # also, has to be a string name for the class' dict.
    setattr(cls, method.__name__, method)




def main():
    dk = DonkeyKong()
    monkeypatch_class(DonkeyKong, coconut_cannon)
    dk.coconut_cannon()


if __name__ == '__main__':
    main()
