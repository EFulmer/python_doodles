def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def fizz_buzz():
    for i in range(1, 101):
        if not (i % 3 == 0 or i % 5 == 0):
            print(i)
        else:
            if i % 3 == 0:
                print('Fizz', end='')
            if i % 5 == 0:
                print('Buzz', end='')
            print('')


def main():
    fizzbuzz()
    fizz_buzz()


if __name__ == '__main__':
    main()
